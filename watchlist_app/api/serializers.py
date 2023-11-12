from rest_framework import serializers


from watchlist_app.models import Movie

# we are creting serializer here it maps each individual element here one by one 
class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only =True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()
    
    
    # we are creating put request by adding normal function
    
    def create(self,validated_data):
         return Movie.objects.create(**validated_data)
     
     
     
    # we are updating the values here 
    # instance hold olv values 
    # validated carries new values
    def update(self,instance,validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.description = validated_data.get('description',instance.description)
        instance.active = validated_data.get('active',instance.active)
        instance.save()
        return instance
        
                