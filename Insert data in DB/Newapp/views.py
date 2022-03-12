from django.shortcuts import render
from rest_framework import viewsets
# from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from newapp.serializers import PersonSerializer
from newapp.models import Person

class PersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed/created/edited/deleted.
    """
    queryset = Person.objects.all().order_by('name')
    serializer_class = PersonSerializer
    # update_data_pk_field = 'name'
	
    # def create(self, request, *args, **kwargs):
    #     kwarg_field: str = self.lookup_url_kwarg or self.lookup_field
    #     self.kwargs[kwarg_field] = request.data[self.update_data_pk_field]

    #     try:
    #         return self.update(request, *args, **kwargs)
    #     except Http404:
    #         return super().create(request, *args, **kwargs)

    # def destroy(self, request, *args, **kwargs):
    #     try:
    #         instance = self.get_object()
    #         instance.delete()
    #     except Http404:
    #         pass
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={
            'request': request,
            'name': self.kwargs.get(self.lookup_url_kwarg)})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)