from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
# from .serializers import restfileSerializer
from django.http import HttpResponse
# from rest_framework import serializers
class RestfileView(APIView):
  parser_classes = (MultiPartParser, FormParser)
  # parser_classe = [restfileParser]
  def post(self, request, format=None):
    # file_serializer = restfileSerializer(data=request.data)
    print(request.data)
    
    return HttpResponse(request.data) 
    # if serializers.is_valid():
    #   serializers.save()
    #   return Response(serializers.data, status=status.HTTP_201_CREATED)
    # else:
    #   return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
   
# def image_upload_2(request):
#     img = file_obj.open(request.FILES["restfile"])    
    