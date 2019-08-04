from rest_framework import views, response, status
from gs123.conversion import BarcodeConverter
from gs123.regex import match_pattern
from quartet_epcis.models import entries
from quartet_epcis.db_api.queries import EPCISDBProxy
from quartet_masterdata.db import DBProxy
from warewolf_api import models
from django.forms.models import model_to_dict


class GetItemDetail(views.APIView):
    queryset = entries.Entry.objects.all()

    def get(self, request, barcode):
        match = match_pattern(barcode)
        ret = None
        if match:
            try:
                db_proxy = DBProxy()
                groupdict = match.groupdict()
                base_id = groupdict.get('gtin14') or groupdict.get('sscc18')
                cpl = db_proxy.get_company_prefix_length(base_id)
                bc = BarcodeConverter(barcode, cpl)
                entry = entries.Entry.objects.get(
                    identifier=bc.epc_urn
                )
                ret = response.Response(model_to_dict(entry))
            except entries.Entry.DoesNotExist:
                pass
            except Exception as e:
                except_str = getattr(e, 'message', repr(e))
                ret = response.Response({'message': except_str},
                                        status=status.HTTP_400_BAD_REQUEST)

        return ret or response.Response(
            {'message': 'The barcode value %s did not '
                        'correlate to any know serialized '
                        'data in the system.' % barcode},
            status=status.HTTP_400_BAD_REQUEST)
