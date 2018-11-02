from machine.models import CsvModel
from rest_framework import serializers


class CsvSerializer(serializers.HyperlinkedModelSerializer):
    csvFile = serializers.FileField()
    imageFile = serializers.ImageField(required=False)

    def create(self,validated_data):
        return CsvModel.objects.create(**validated_data)

    class Meta:
        model = CsvModel
        fields = ('pk', 'csvFile','imageFile')