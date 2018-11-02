from django.conf.urls import include, url

from rest_framework import routers
from machineRest import views

routers = routers.DefaultRouter()

routers.register('machine',views.CsvViewSet, 'machine')


urlpatterns = [
    url(r'^',include(routers.urls))
]