from django.shortcuts import render
from rest_framework import  generics

# Create your views here.
from webservice.models import sanlp
from webservice.serializers import sanlpserializer


class ListCreatesanlp(generics.ListCreateAPIView):
    queryset = sanlp.objects.all()
    serializer_class = sanlpserializer

class ListDetailsforpid(generics.ListCreateAPIView):
    #queryset = sanlp.objects.get(p_id= )