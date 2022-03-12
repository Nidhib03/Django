from rest_framework import serializers
from .models import Restfile
class RestfileSerializer(serializers.ModelSerializer):
  class Meta():
    model = Restfile
    fields = ('file', 'remark', 'timestamp')