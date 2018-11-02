from .models import CsvModel
from rest_framework import serializers


class CsvSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CsvModel
        fields = ('pk', 'csvFile', 'name','imageFile')
