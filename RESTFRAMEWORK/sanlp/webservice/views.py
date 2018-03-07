from django.shortcuts import render
from rest_framework import  generics
from rest_framework.decorators import api_view
from webservice.serializers import sanlpserializer
from pymongo import MongoClient
from rest_framework.response import Response

# Create your views here.
@api_view(['GET', 'POST', ])
def get_product(request):

    #connecting mongodb
    databaseName = "sanl"
    connection = MongoClient()
    db = connection[databaseName]
    details = db['sanlp']

    #collecting query_parameters
    query_param={'p_id':None,'date':None}
    list1=request.GET.urlencode().split('&')
    try:
        for l in list1:
            query_param[str(l.split('=')[0])] = str(l.split('=')[1])
    except:
        None #no parameter

    #both p_id and date available as query_parameter
    if query_param['p_id'] != None and query_param['date'] != None:
        data= details.find({'p_id': query_param['p_id']})
        for d in data:
            for i in range(len(d['review_detail'])):
                if d['review_detail'][i]['date'] == query_param['date']:
                    d1 = {}
                    d1['p_id'] = d['p_id']
                    d1['p_name'] = d['p_name']
                    d1['review_detail'] = d['review_detail'][i]
                    serializer = sanlpserializer(d1, many=False)
                    return Response(serializer.data)

    #only p_id available as query_parameter
    elif query_param['p_id'] != None and query_param['date'] == None:
        serializer = sanlpserializer(details.find({'p_id': query_param['p_id']}), many=True)
        return Response(serializer.data)

    #only date available as query_parameter
    elif query_param['p_id'] == None and query_param['date'] != None:
        l1 = []
        for d in details.find():
            for i in range(len(d['review_detail'])):
                if d['review_detail'][i]['date'] == query_param['date']:
                    d1 = {}
                    d1['p_id'] = d['p_id']
                    d1['p_name'] = d['p_name']
                    d1['review_detail'] = d['review_detail'][i]
                    l1.append(d1)
        serializer = sanlpserializer(l1, many=True)
        return Response(serializer.data)

    #no parameter is available
    else:
        serializer = sanlpserializer(details.find(), many=True)
        return Response(serializer.data)




    '''try:
    #approach 1
        p_id=str(request.GET['p_id'])
        try:
            date=str(request.GET['date'])
            for d in details.find({'p_id':p_id}):
                for i in range(len(d['review_detail'])):
                    if d['review_detail'][i]['date'] == date:
                        d1={}
                        d1['p_id']=d['p_id']
                        d1['p_name']=d['p_name']
                        d1['review_detail']=d['review_detail'][i]
                        serializer = sanlpserializer(d1, many=False)
                        return Response(serializer.data)
        except:
            serializer = sanlpserializer(details.find({'p_id':p_id}), many=True)
            return Response(serializer.data)
    except:
        try:
            l1=[]
            date = str(request.GET['date'])
            for d in details.find():
                for i in range(len(d['review_detail'])):
                    if d['review_detail'][i]['date'] == date:
                        d1={}
                        d1['p_id']=d['p_id']
                        d1['p_name']=d['p_name']
                        d1['review_detail']=d['review_detail'][i]
                        l1.append(d1)
            serializer = sanlpserializer(l1, many=True)
            return Response(serializer.data)
        except:
            serializer = sanlpserializer(details.find(), many=True)
            return Response(serializer.data)
    '''