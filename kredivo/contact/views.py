from django.shortcuts import render

from rest_framework import viewsets
from .models import Contact
from .serializers import ContactSerializer
# from rest_framework.parsers import FileuploadParser
# from rest_framework.response import Response
# from rest_framework import status 
# Create your views here.

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    # parser_class = (FileuploadParser)

    # def post(self, request, *args, **kwargs):
    #     contactSerializer = ContactSerializer(data=request.data)
    #     if contactSerializer.is_valid():
    #         contactSerializer.save()
    #         return Response(contactSerializer.data, status = status.HTTP_201_CREATED)
