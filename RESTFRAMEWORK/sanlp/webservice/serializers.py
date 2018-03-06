from rest_framework import serializers
from webservice.models import sanlp


class sanlpserializer(serializers.ModelSerializer):
    class Meta:
        model=sanlp
        fields=('id','p_id','p_name','review_detail')