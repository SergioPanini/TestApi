from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
import time

from .models import APPModels
from .serializer import AppGetSerializer, AppPostSerializer

def MainPage(request):
    return HttpResponse('it is work')

class AppView(APIView):
    
    def get(self, request, KeyApi):
        SelectApp = get_object_or_404(APPModels.objects.all(),KeyApi=KeyApi)
        ser = AppGetSerializer(SelectApp)
        
        return Response({'app': ser.data})
    
    def post(self, request, KeyApi):
        data = request.data.get('app')

        ser = AppPostSerializer(data=data)
        if ser.is_valid(raise_exception=True):
            print(ser)
            new_app = ser.save()
            print(new_app)
            new_app.KeyApi = str(time.time())
            new_app.save()
        
        return Response({'success':'{}'.format(new_app.KeyApi)}) 

class CreateNewKeyApiView(APIView):
    def get(self, request, KeyApi):
        SelectApp = get_object_or_404(APPModels.objects.all(), KeyApi=KeyApi)
        NewKeyApi = str(time.time())

        SelectApp.KeyApi = NewKeyApi
        return Response({'app':{'Name': SelectApp.Name, 'OldKeyApi': KeyApi, 'NewKeyApi': NewKeyApi}})

class APPModelsView(APIView):

    def get(self, request):
        apps = APPModels.objects.all()

        ser = AppSerializer(apps, many=True)
        return Response({'apps': ser.data})
    
    def post(self, request):
        print(request.data.get('app'))
    
        return Response('good')

    
