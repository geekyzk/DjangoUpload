from django.shortcuts import render

from rest_framework import viewsets
from .serializers import CsvSerializer
from django.http import request
from rest_framework.views import APIView, Response
from machine.models import CsvModel
from django.core.files.storage import default_storage
from django.core.files.uploadedfile import  SimpleUploadedFile
from django.core.files.uploadedfile import InMemoryUploadedFile

from django.core.files.base import ContentFile
import os
from yinlzDjango.settings import MEDIA_ROOT

# Create your views here.
class CsvViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CsvModel.objects.all()
    serializer_class = CsvSerializer

    def create(self, request, *args, **kwargs):
        file_ = request.data['csvFile']
        print(type(file_))
        media_file = default_storage.save('csv.jpg',ContentFile(file_.read()))
        # path为csv数据文件路径
        path = os.path.join(MEDIA_ROOT,media_file)
        print(path)

        # todo 图片训练代码

        # 下面这个paht替换成训练后生成图片的路径
        f = open(path,'rb')

        request.data['imageFile'] = SimpleUploadedFile(media_file, f.read(), file_.content_type)
        request.FILES['imageFile'] = SimpleUploadedFile(media_file, f.read(), file_.content_type)
        response = super(CsvViewSet, self).create(request, *args, **kwargs)
        return response

