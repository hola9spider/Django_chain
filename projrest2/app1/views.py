from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from app1.models import App
from app1.serializers import AppSerializer

def app_list(request):
    if request.method == 'GET':
        app1 = App.objects.all()
        serializer = AppSerializer(app1)
        return JsonResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AppSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
