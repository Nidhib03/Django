from rest_framework import serializers 
from newapp.models import Person
 
 
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['name', 'branch', 'roll', 'age']
        # extra_kwargs = {"age":{'required':False}}