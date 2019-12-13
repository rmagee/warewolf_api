from rest_framework import views, response, status
from copy import copy
from gs123.conversion import BarcodeConverter
from gs123.regex import match_pattern
from quartet_epcis.models import entries
from quartet_masterdata.db import DBProxy
from quartet_epcis.db_api.queries import EPCISDBProxy
from quartet_masterdata.models import TradeItem
from warewolf_api import serializers


class GetItemDetail(views.APIView):
    queryset = entries.Entry.objects.none()
    serializer_class = serializers.EntrySerializer

    def get(self, request, barcode=None):
        """
        Will attempt to convert the barcode to a URN to lookup within the
        quartet_epcis.models.entries.Entry table to get relevant information
        about the item in question.
        :param request: The HTTP request.
        :param barcode: The barcode in question.
        :return: The Entry serialized to JSON or will raise 400 if the
            value could not be found or there was not a proper company or
            trade item configured to allow the system to lookup the company
            prefix length.
        """
        ret = None
        if barcode == None:
            ret = response.Response(
                'No barcode provided.',
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            try:
                epc = None
                lot = None
                if barcode.startswith('urn'):
                    epc = barcode
                else:
                    match = match_pattern(barcode)
                    if match:
                        db_proxy = DBProxy()
                        groupdict = match.groupdict()
                        base_id = groupdict.get('gtin14') or groupdict.get(
                            'sscc18')
                        lot = groupdict.get('lot')
                        cpl = db_proxy.get_company_prefix_length(base_id)
                        epc = BarcodeConverter(barcode, cpl).epc_urn
                    else:
                        # SSCCs will always match above so we only need to
                        # check for oddly formatted GTINs
                        if barcode.startswith('01'):
                            gtin14 = barcode[2:16]
                            cpl = DBProxy().get_company_prefix_length(gtin14)
                            snl = TradeItem.objects.get(
                                GTIN14=gtin14).serial_number_length
                            epc = BarcodeConverter(barcode,
                                                   company_prefix_length=cpl,
                                                   serial_number_length=snl)

                entry = entries.Entry.objects.select_related('parent_id',
                                                             'top_id',
                                                             'last_event',
                                                             'last_aggregation_event').only(
                    'parent_id__identifier',
                    'top_id__identifier',
                    'last_event__event_time',
                    'last_aggregation_event__event_time'
                ).get(
                    identifier=epc
                )
                vals = {}
                if entry:
                    events = EPCISDBProxy().get_object_events_by_epcs(
                        [entry.identifier], select_for_update=False)
                    for event in events:
                        if len(event.ilmd) > 0:
                            vals.update({i.name: i.value for i in event.ilmd})
                entry.ilmd = vals
                data = serializers.EntrySerializer(entry)
                ret = response.Response(data.data)

            except entries.Entry.DoesNotExist:
                pass
            except TradeItem.DoesNotExist:
                ret = response.Response(
                    {'message':
                         'The GTIN/TradeItem for that barcode could not be '
                         'located or it does not have a company and/or '
                         'serial number length defined.',
                     }, status=status.HTTP_400_BAD_REQUEST
                )
            except DBProxy.CompanyConfigurationError as cce:
                except_str = getattr(cce, 'message', repr(cce))
                ret = response.Response({'message': except_str},
                                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            except Exception as e:
                except_str = getattr(e, 'message', repr(e))
                ret = response.Response({'message': except_str},
                                        status=status.HTTP_400_BAD_REQUEST)
        return ret or response.Response(
            {
                'message': 'Could not find value "%s" in the system.'
                           % barcode
            },
            status=status.HTTP_400_BAD_REQUEST)
