from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Movie
from .serializers import MovieSerializer
from django.core.paginator import Paginator
from django.db.models import Count

# Create your views here.

@api_view(['GET'])
def welcome(request):
    return Response({'message':'Movies API'}, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_all_movies(request):
    try:
        title = request.query_params.get('title')
        rating = request.query_params.get('rating')
        country = request.query_params.get('country')
        page_number = int(request.query_params.get('page', 1))
        page_size = int(request.query_params.get('page_size', 10))
        ordering = request.query_params.get('ordering', 'title')
        movies = Movie.objects.all()
        
        if(page_number < 1):
            page_number = 1
        if(page_size < 1):
            page_size = 10
        
        if title:
            movies = movies.filter(title__icontains=title)
        if rating:
            movies = movies.filter(rating=rating)
        if country:
            movies = movies.filter(country__icontains=country)
        
        movies = movies.order_by(ordering)
            
        paginator = Paginator(movies, page_size)
        page_obj = paginator.get_page(page_number)
        
            
        serializer = MovieSerializer(page_obj, many=True)
        return Response({
            'count': paginator.count,
            'page_count': paginator.num_pages,
            'current_page': page_obj.number,
            'success':True,
            'data': serializer.data
        })
    except Exception as e:
        return Response({
            'success': False,
            'error': str(e)
        }, status=500)

@api_view(['GET'])
def get_movie_by_id(request, id):
    try:
        movie = Movie.objects.get(id=id)
        serializer = MovieSerializer(movie)
        return Response({
            'success': True,
            'data': [serializer.data]
        })
    except Movie.DoesNotExist:
        return Response({
            'success': False,
            'error': 'Movie not found with the given id.'
        }, status=404)
    except Exception as e:
        return Response({
            'success': False,
            'error': str(e)
        }, status=500)

@api_view(['DELETE'])
def delete_movie_by_id(request, id):
    movie = Movie.objects.get(id=id)
    movie.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def search_movies(request):
    query = request.query_params.get('query', '')
    movies = Movie.objects.filter(title__icontains=query) | \
             Movie.objects.filter(rating__icontains=query) | \
             Movie.objects.filter(country__icontains=query) | \
             Movie.objects.filter(id__icontains=query)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def modify_movie_by_id(request, id):
    movie = Movie.objects.get(id=id)
    serializer = MovieSerializer(movie, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_movie(request):
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_summary(request):
    try:
        countries = Movie.objects.values('country').annotate(count_pais=Count('country')).order_by('country')
        ratings = {}
        for i in range(1, 6):
            ratings[f'count_calificacion_{i}'] = Movie.objects.filter(rating=i).count()
        
        country_data = {
            f'count_{country["country"]}':country['count_pais']
            for country in countries
        }

        summary_data = {
            'success': True,
            'data': [{**country_data,**ratings}]
        }
        return Response(summary_data)
    except Exception as e:
        return Response({
            'success': False,
            'error': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_top_movies(request):
    top_movies = Movie.objects.order_by('-rating')[:5]
    top_movies_data = [{'title': movie.title, 'rating': movie.rating} for movie in top_movies]
    return Response(top_movies_data)
