from rest_framework import serializers


# we are creting serializer here it maps each individual element here one by one 
class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only =True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()