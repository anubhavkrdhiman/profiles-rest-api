from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """serializes a name field for testint our APIVIEW"""
    name = serializers.CharField(max_length=10)
    age = serializers.CharField(max_length=2)
