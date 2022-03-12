from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from postapp.serializers import FileSerializer


class FileUploadViewSet(viewsets.ViewSet):

    def create(self, request):
        # print("data::::::::::::::",request.data)
        # print("***********fname*",request.POST['fname'])
        # return Response({'first name':request.POST['fname'],"last name":request.POST['lname'],'Email':request.POST['email'],'mono':request.POST['mono']})
        serializer_class = FileSerializer(data=request.data)
        
        if 'fname' in request.FILES or serializer_class.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        else:
            #Single File
            print("Response info!")
            # handle_uploaded_file(request.POST['file])
            
            #Multiple Files
            # postapps = request.FILES.getlist('file')
            # for f in postapps:
            #     handle_uploaded_file(f)

            return Response({'first name':request.POST['fname'],"last name":request.POST['lname'],'Email':request.POST['email'],'mono':request.POST['mono']},status=status.HTTP_201_CREATED)

# def handle_uploaded_file(f):
#     with open(f.name, 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)
