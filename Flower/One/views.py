from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser


from .serializer import AppSer, testser
from .models import Apps

import time

class AppView(APIView):

    def get(self, request, KeyApi):
        new_app = get_object_or_404(Apps.objects.all(), KeyApi=KeyApi)
        Ser = AppSer(new_app)

        return Response({"app":Ser.data})

    def post(self, request, KeyApi):
        data = request.data.get('newapp')
        if type(data) != 'dict':
            data = {'KeyApi':''}

        data['KeyApi'] = time.time()
        
        Ser = AppSer(data=data)
        NewKeyApi = ''
            
        if Ser.is_valid():
            NewKeyApi = Ser.save().KeyApi
            saved = True
        else:
            saved = False
        return Response({'success':'{}'.format(saved), 'KeyApi': NewKeyApi})
    
    def put(self, request, KeyApi):
        SelectApp = get_object_or_404(Apps.objects.all(), KeyApi=KeyApi)
        data = request.data.get('updateapp')
        if type(data) != 'dict':
            data = {'':''}
        
        Ser = AppSer(instance=SelectApp, data=data, partial=True)

        if Ser.is_valid(raise_exception=True):
            Ser.save()
            saved = True
        else:
            saved = False

        return Response({'success': '{}'.format(saved)})








def MainPage(request):
    ser = testser(data={'Name': 'testname', 'sisk':'ggvp'})
    if ser.is_valid():
        saved = ser.save().Name
    return HttpResponse('it is work: {}'.format(saved))

    