from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from backend.celery import add
from celery.result import AsyncResult
# Create your views here.

@api_view(['GET'])
def check_result(request):
    q  = request.query_params
    result = AsyncResult(q.get('task_id'))
    return Response({'state':result.state,'id':result.id, 'result':result.result,"status":result.status})


@api_view(['GET'])
def task(request):
    t = add.delay(10,20)
    return Response(str(t))









