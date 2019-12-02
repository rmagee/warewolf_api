from rest_framework import views, response, status

from gs123.conversion import BarcodeConverter
from gs123.regex import match_pattern
from quartet_epcis.models import entries
from quartet_masterdata.db import DBProxy
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
                if barcode.startswith('urn'):
                    epc = barcode
                else:
                    match = match_pattern(barcode)
                    if match:
                        db_proxy = DBProxy()
                        groupdict = match.groupdict()
                        base_id = groupdict.get('gtin14') or groupdict.get(
                            'sscc18')
                        cpl = db_proxy.get_company_prefix_length(base_id)
                        epc = BarcodeConverter(barcode, cpl).epc_urn
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
                ret = response.Response(serializers.EntrySerializer(entry).data)
            except entries.Entry.DoesNotExist:
                pass
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
