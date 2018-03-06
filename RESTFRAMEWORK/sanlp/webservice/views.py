from django.shortcuts import render
from rest_framework import  generics

# Create your views here.
from rest_framework.decorators import api_view


from webservice.serializers import sanlpserializer
from pymongo import MongoClient
from rest_framework.response import Response
@api_view(['GET', 'POST', ])
def all_product(request):
    databaseName = "sanl"
    connection = MongoClient()
    db = connection[databaseName]
    details = db['sanlp']
    print(details)
    serializer = sanlpserializer(details, many=False)
    return Response(serializer.data)


@api_view(['GET', 'POST', ])
def get_product(request):
    databaseName = "sanl"
    connection = MongoClient()
    db = connection[databaseName]
    details = db['sanlp']
    try:
        p_id=str(request.GET['p_id'])
        date=str(request.GET['date'])
        print(date)
        for d in details.find({'p_id':p_id}):
            #print(d)
            for i in range(len(d['review_detail'])):
                if d['review_detail'][i]['date'] == date:
                    d1={}
                    d1['p_id']=d['p_id']
                    d1['p_name']=d['p_name']
                    d1['review_detail']=d['review_detail'][i]
                    serializer = sanlpserializer(d1, many=False)
                    return Response(serializer.data)
            #print(d["p_name"])
    except:
        serializer = sanlpserializer(details.find(), many=True)
        return Response(serializer.data)