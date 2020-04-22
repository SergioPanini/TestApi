from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser


from .serializer import AppSer
from .models import Apps

import time

class AppView(APIView):

    def get(self, request, KeyApi):
        new_app = get_object_or_404(Apps.objects.all(), KeyApi=KeyApi)
        Ser = AppSer(new_app)

        return Response({"app":Ser.data})

    def post(self, request, KeyApi):
        data = request.data.get('newapp')
        data['KeyApi'] = time.time()
        
        Ser = AppSer(data=data)
        
        if Ser.is_valid():
            saved = Ser.save().KeyApi
        else:
            saved = False
        return Response({'success':'{}'.format(saved)})



def MainPage(request):
    new_app = Apps.objects.create(Name='MarkUp', Des='marketplace')
    
    Ser = Test(new_app)

    return HttpResponse('it is work: ', Ser.data)

    