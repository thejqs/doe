#!usr/bin/env python

"""

A scrape script to take a person's IMDB page, open the filmography urls
and then each movie page and capture the cast and crew of each movie.
The one provided is for Arthur Piantadosi, sound man and my grandfather.

In progress. Emphasis on movies for now.


"""

#----------------------------//IMPORTS
import django
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
import sys, os
import urllib
import urllib2
from lxml import etree
import StringIO
import string

import unicodedata
import itertools
#----------------------------//APP IMPORTS
sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

django.setup()
from main.models import Arthur, Movie, CastMember, CrewMember



class Scraper():

    # to ensure we have a valid url to read
    @staticmethod
    def open_url(url):
        click = urllib.urlopen(url)
        if click.getcode() == 200:
            html = click.read()
            return html
        else:
            raise Exception("Nice try. Bad link.")

    # to produce a parsed html tree
    @staticmethod
    def parse_html(html):
        parser = etree.HTMLParser()
        tree = etree.parse(StringIO.StringIO(html), parser)

        return tree

    # captures the movie name and url
    # stores them as {title: url}
    @staticmethod
    def capture_filmography(url):
        html = Scraper.open_url(url)
        tree = Scraper.parse_html(html)

        movies_xpath = '//*[@id="filmography"]/div[2]/div/b/a/text()'
        href_xpath = '//*[@id="filmography"]/div[2]/div/b/a/@href'

        movies = tree.xpath(movies_xpath)
        hrefs = tree.xpath(href_xpath)
        # a dictionary to hold movie name and link value together
        movie_links = {}
        for i in range(0, len(movies)):
            movie_links[movies[i]] = hrefs[i]

        return movie_links

    # pulls together all the contextual elements related to each movie
    # with the title as the key
    @staticmethod
    def collect_context(movie_tree, movie_html, cast_crew_tree):

        movie_title_xpath = '//*[@id="overview-top"]/h1/span[1]/text()'
        movie_title = movie_tree.xpath(movie_title_xpath)[0]
        print movie_title

        if "<h2>Episodes" not in movie_html:
            movie_year_xpath = '//*[@id="main"]/div[1]/div[1]/div/h3/span/text()'
            genre_xpath = '//*[@id="overview-top"]/div[2]/a/span/text()'

        else:
            # movie_year_xpath = '//*[@id="overview-top"]/h1/span[2]/text()'
            # genre_xpath = '//*[@id="overview-top"]/div[1]/a/span/text()'
            print "Yep. TV show. Do not want."

        movie_year = cast_crew_tree.xpath(movie_year_xpath)
        if len(movie_year) == 1:
            movie_year_final = Scraper.clean_int_from_ugly_string(movie_year)
        else:
            # not my favorite to hard-code it. temporary as I worked out an issue with
            # TV shows -- of which there is only one involved here.
            # movie_year_final = 1962
            print "Like I said about that whole TV show thing."
        # print type(movie_year_final)

        movie_genre = movie_tree.xpath(genre_xpath)
        all_genres = [genre for genre in movie_genre]

        description_xpath = '//*[@id="overview-top"]/p[2]/text()'
        description = movie_tree.xpath(description_xpath)[0]
        description = description.strip()
        # print type(description)
        # print description

        all_context = {}

        all_context[movie_title] = [movie_year_final, all_genres, description]

        movie, created = Movie.objects.get_or_create(
            title=movie_title,
            year_released=movie_year_final,
            genre=all_genres,
            description=description
        )

        poster_xpath = '//*[@id="img_primary"]/div[1]/a/img/@src'
        poster = movie_tree.xpath(poster_xpath)
        if len(poster) == 1:
            poster = poster[0]
            poster_response = urllib.urlopen(poster).read()
            poster_temp = NamedTemporaryFile(delete=True)
            poster_temp.write(poster_response)
            movie.poster.save('%s.jpg' % movie_title, File(poster_temp))
            movie.save()
        else:
            # one movie with no poster. what even is life.
            print "Ain't no poster here."
        # movie.save()

        return all_context

    # cleans up the movie year, which comes in as, you guessed it,
    # an ugly string.
    # should work on any string where the number values in existing order
    # are all you want returned.
    # and yes I just wrote more comment lines than lines of code.
    @staticmethod
    def clean_int_from_ugly_string(movie_year):
        movie_year = movie_year[0]
        wash_num = string.maketrans('', '')
        scrub_num = wash_num.translate(wash_num, string.digits)

        return int(movie_year.translate(wash_num, scrub_num))

    # opens a movie page and finds the cast and crew link
    # also cleans up the movie link to remove the reference string
    @staticmethod
    def find_coworkers(href):
        movie_html = Scraper.open_url("http://www.imdb.com%s" % href)
        movie_tree = Scraper.parse_html(movie_html)

        if '<h2>Episodes' not in movie_html:
            cast_crew_href_xpath = '//*[@id="overview-top"]/div[6]/span[2]/a/@href'
        else:
            # cast_crew_href_xpath = '//*[@id="overview-top"]/div[3]/span[2]/a/@href'
            print "This is a TV show. Ignore it."

        cast_crew_href = movie_tree.xpath(cast_crew_href_xpath)

        naked_href = href.split('?', 1)[0]

        # print "http://www.imdb.com%s%s" % (naked_href, cast_crew_href[0])
        return "http://www.imdb.com%s%s" % (naked_href, cast_crew_href[0]), movie_tree, movie_html

    # targets the movie title, year released and cast and crew data
    # cleans up the title and year
    @staticmethod
    def get_coworkers(url):
        cast_crew_html = Scraper.open_url(url)
        cast_crew_tree = Scraper.parse_html(cast_crew_html)

        cast_crew_jobs_xpath = '//*[@id="fullcredits_content"]/h4/text()'

        cast_crew_jobs = cast_crew_tree.xpath(cast_crew_jobs_xpath)

        return cast_crew_jobs, cast_crew_html, cast_crew_tree

    # the scraper itself, given a page on which to begin
    @staticmethod
    def scrape():
        movie_links = Scraper.capture_filmography("http://www.imdb.com/name/nm0681250/?ref_=fn_al_nm_1")

        Movie.objects.all().delete()
        CastMember.objects.all().delete()
        CrewMember.objects.all().delete()

        for movie, href in movie_links.items():
            # this is the only TV show on this particular list.
            # resolved about half the issues with scraping it
            # and will have to cme back to this.
            if movie != "The Jack Benny Program":

                cast_and_crew_url, movie_tree, movie_html = Scraper.find_coworkers(href)

                cast_crew_jobs, cast_crew_html, cast_crew_tree = Scraper.get_coworkers(cast_and_crew_url)

                all_context = Scraper.collect_context(movie_tree, movie_html, cast_crew_tree)
                # print context

                cast_crew_data = Scraper.scrape_data(cast_crew_jobs, cast_crew_html, cast_crew_tree)

            # print movie #, cast_crew_data

    # grabs the main target data, does the heaviest lifting
    @staticmethod
    def scrape_data(cast_crew_jobs, cast_crew_html, cast_crew_tree):

        # prepares for a loop
        current_credit = 0
        current_job_title = 0

        # to store the loop results as {job type: [cast and crew members]}
        cast_and_crew = {}

        job_titles = {}

        merged_dict = {}

        for job in cast_crew_jobs:

            # just getting rid of some ugly whitespace around some job types
            job = job.strip()

            # skips a couple empty lines that desynchronize jobs and cast/crew
            if not job:
                continue

            # cast has a different xpath, so need to grab that separately
            if 'Cast' != job: #and 'Series Cast' != job:
                # print "%r" % job.strip()

                # table values begin at 1; we want to go through them all
                crew_name_xpath = '//*[@id="fullcredits_content"]/table[%d]/tbody/tr/td[1]/a/text()' % (current_credit + 1)
                crew_job_xpath = '//*[@id="fullcredits_content"]/table[%d]/tbody/tr/td[3]/text()' % (current_job_title + 1)

                # strips trailing newline characters off crew members' names
                # also decomposes unicode/ascii values to base characters
                cast_and_crew[job] = [name.strip() if isinstance(name, str) else unicodedata.normalize('NFKD', name.strip()).encode('ascii', 'ignore') for name in cast_crew_tree.xpath(crew_name_xpath)]

                # but if you're thinking this is the ugliest list comprehension
                # in the known universe, you're not wrong
                # gives me something to come back to later now that it works
                job_titles[job] = [title.strip() if isinstance(title, str) else unicodedata.normalize('NFKD', title.strip()).encode('ascii', 'ignore') for title in cast_crew_tree.xpath(crew_job_xpath)]

            else:
                # if 'Series Cast' not in cast_crew_html:
                cast_name_xpath = '//*[@id="fullcredits_content"]/table[3]/tr/td/a/span/text()'

                # else:
                #     cast_name_xpath = '//*[@id="cast"]/text()[1]'

                # character names come in on two different xpaths, so that can
                # be something I add later

                cast_and_crew[job] = [name.strip() if isinstance(name, str) else unicodedata.normalize('NFKD', name.strip()).encode('ascii', 'ignore') for name in cast_crew_tree.xpath(cast_name_xpath)]


            # increments to the next job
            current_credit += 1
            current_job_title += 1

        for category, names in cast_and_crew.items():
            if category != 'Cast': # or category != 'Series Cast':
                # print job_titles
                jobs = job_titles.get(category, [])
                temp = list(itertools.izip_longest(names, jobs))
                # print temp
                # print type(temp)
                # for l in temp: print l

                merged_dict[category] = temp

            merged_dict['Cast'] = cast_and_crew['Cast']

        for category, crew in merged_dict.items():
            # names, jobs = zip(*crew)
            if category != 'Cast': # or category != 'Series Cast':
                for person, title in crew:
                    print category
                    print person
                    print title
                    print "\n\n"
                    crew = CrewMember.objects.create(name=person, job_title=title)


        # merged_dict['Series Cast'] = cast_and_crew['Series Cast']

        # print merged_dict

        for actor in merged_dict['Cast']:
            print 'Cast'
            print actor
            print "\n\n"
            name = CastMember.objects.create(name=actor)

    # merged_dict['Series Cast'] = cast_and_crew['Series Cast']

    # for actor in merged_dict['Series Cast']:
    #     print category
    #     print actor
    #     print "\n\n"
    #     name, created = CastMember.objects.get_or_create(name=actor)

        return merged_dict


Scraper.scrape()
