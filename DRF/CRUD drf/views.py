from http.client import HTTPResponse
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from resapp.models import Reapp
from resapp.serializers import ReappSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def reapp_list(request):
    # GET list of resapp, POST a new reapp, DELETE all resapp
    print("DONE")
    
    # Retrieve objects(with condition)
    if request.method == 'GET':
        resapp = Reapp.objects.all()
        
        name = request.GET.get('name', None)
        print("name:::::::::::::::::::::",name)
        if name is not None:
            resapp = resapp.filter(name__icontains=name)
            print("resapp:::::::::::::",resapp)
            
        resapp_serializer = ReappSerializer(resapp, many=True)
        return JsonResponse(resapp_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    
    # Create a new object
    elif request.method == 'POST':
        reapp_data = JSONParser().parse(request)
        reapp_serializer = ReappSerializer(data=reapp_data)
        if reapp_serializer.is_valid():
            reapp_serializer.save()
            return JsonResponse(reapp_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(reapp_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Delete all objects
    elif request.method == 'DELETE':
        count = Reapp.objects.all().delete()
        return JsonResponse({'message': '{} Resapp were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

 
@api_view(['GET', 'PUT', 'DELETE'])
def reapp_detail(request, name):                          # methods with pk (primary key) write pk insteed of name everywhere
    try: 
        reapp = Reapp.objects.get(name=name) 
    except Reapp.DoesNotExist:
        return JsonResponse({'message': 'The reapp does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        reapp_serializer = ReappSerializer(reapp)
        return JsonResponse(reapp_serializer.data)
    
    # Update an object
    elif request.method == 'PUT':
        reapp_data = JSONParser().parse(request)
        reapp_serializer = ReappSerializer(reapp, data=reapp_data)
        if reapp_serializer.is_valid():
            reapp_serializer.save()
            return JsonResponse(reapp_serializer.data)
        return JsonResponse(reapp_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Delete an object 
    if request.method == 'DELETE':
        reapp.delete()
        return JsonResponse({'message': 'reapp was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
    

@api_view(['GET','DELETE'])
def reapp_list_info(request):
    resapp = Reapp.objects.filter()        
    if request.method == 'GET': 
        print("call")
        name = request.GET.get('name', None)
        print(name)
        # resapp_serializer = ReappSerializer(resapp, many=True)
        return JsonResponse({"name": "ok"})
    
    if request.method == "DELETE":
        print("Deleted")
        resapp.delete()
        return JsonResponse({'message': 'reapp was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        