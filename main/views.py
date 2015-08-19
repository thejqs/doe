from django.shortcuts import render, render_to_response
# from django.template import RequestContext
# from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from collections import OrderedDict
import ast

# import re

# from django.views.generic.list import ListView

from main.models import Arthur, Movie, CrewMember, CastMember

# Create your views here.


def movies(request):
    context = {}
    movies_by_year = OrderedDict()

    movies = Movie.objects.all().order_by('year_released')

    for movie in movies:
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
    print movies_by_year

    return render(request, 'movies.html', context)
