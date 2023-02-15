from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from task_service.celery import async_task

@api_view(['GET'])
def task(request):
    if request.method == 'GET':
        async_task.delay()
        return HttpResponse("Created a task")
