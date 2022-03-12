from rest_framework import serializers 
from resapp.models import Reapp
 
 
class ReappSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Reapp
        fields = ('id',
                  'name',
                  'adhar_no',
                  'mail')