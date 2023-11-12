from rest_framework.response import Response
from rest_framework.decorators import api_view

from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer

@api_view(['GET','POST'])
def movie_list(request):
    if request.method =='GET':
        
        movies = Movie.objects.all()
        # we use many = true because we want to fetch all data becausen we are using function based view 
        # also have multiple objects here
        serializer = MovieSerializer(movies,many=True)
        # we use data method here to fetch all data 
        return Response(serializer.data)
    if request.method =='POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['GET'])
def movie_details(request,pk):
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)