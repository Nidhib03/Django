from rest_framework import serializers

class FileSerializer(serializers.Serializer):
    # file = serializers.FileField(max_length=None, allow_empty_file=False)
    
    fname = serializers.CharField(max_length=20)
    lname = serializers.CharField(max_length=20)
    email = serializers.EmailField( max_length=None)
    mono = serializers.IntegerField(max_value=10)