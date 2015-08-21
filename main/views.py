from django.shortcuts import render, render_to_response
# from django.template import RequestContext
# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from collections import OrderedDict
import ast

# import re

# from django.views.generic.list import ListView

from main.models import Arthur, Movie, CrewMember, ArthurGrandchild

# Create your views here.


def arthur(request):
    return render(request, 'arthur.html')


def movies(request):
    context = {}
    movies_by_year = OrderedDict()
    arthur_grandchildren = {}

    movies = Movie.objects.all().order_by('year_released')

    arthur = Arthur.objects.first()
    # arthur = Arthur.objects.values('born', 'died', 'moved_to_la', 'married_year')

    grandchildren = ArthurGrandchild.objects.all()

    for movie in movies:

        count = 0

        for grandchild in grandchildren:
            if movie.year_released >= grandchild.born:
                year_dif = grandchild.born - movie.year_released
                count += 1
            else:
                pass

        movie.grandchild_count = count

        movie.arthur_married = movie.year_released - arthur.married_year
        # [0]['married_year']

        movie.arthur_in_la = movie.year_released - arthur.moved_to_la
        # [0]['moved_to_la']

        movie.age = movie.year_released - arthur.born
        # [0]['born']

        movie.genres = ast.literal_eval(movie.genre)

        try:
            movies_by_year[movie.year_released].append(movie)
        except:
            movies_by_year[movie.year_released] = [movie]


            #     'title': movie.title,
            #     'year': movie.year_released,
            #     'genre': movie.genre.replace("'", ""),
            #     'poster': movie.poster,
            #     'desc': movie.description
            # }
        # print movies_dict
    context['movies'] = movies_by_year
    # context['arthur'] = arthur
    # print movies_by_year

    return render(request, 'movies.html', context)


def cast_and_crew(request):
    context = {}



    return render(request, context)
