#!usr/bin/env python

import urllib
import urllib2
import StringIO
import re, sys, os
import string

from lxml import etree

import unicodedata

result = urllib.urlopen("http://www.imdb.com/name/nm0681250/?ref_=fn_al_nm_1")
html = result.read()

parser = etree.HTMLParser()
tree = etree.parse(StringIO.StringIO(html), parser)

movies_xpath = '//*[@id="filmography"]/div[2]/div/b/a/text()'
href_xpath = '//*[@id="filmography"]/div[2]/div/b/a/@href'

movies = tree.xpath(movies_xpath)
hrefs = tree.xpath(href_xpath)

for movie in movies:
    for href in hrefs:

        movie_result = urllib.urlopen("http://www.imdb.com%s" % href)

        cast_crew_html = movie_result.read()
        cast_crew_tree = etree.parse(StringIO.StringIO(cast_crew_html), parser)

        cast_crew_href_xpath = '//*[@id="overview-top"]/div[6]/span[2]/a/@href'
        cast_crew_href = cast_crew_tree.xpath(cast_crew_href_xpath)

        naked_href = href.split('?', 1)[0]

        cast_crew_result = urllib.urlopen("http://www.imdb.com%s%s" % (naked_href, cast_crew_href[0]))
        cast_crew_html = cast_crew_result.read()
        cast_crew_tree = etree.parse(StringIO.StringIO(cast_crew_html), parser)

        movie_title_xpath ='//*[@id="main"]/div[1]/div[1]/div/h3/a/text()'
        movie_title = cast_crew_tree.xpath(movie_title_xpath)

        cast_crew_jobs_xpath = '//*[@id="fullcredits_content"]/h4/text()'
        cast_crew_jobs = cast_crew_tree.xpath(cast_crew_jobs_xpath)

        current_credit = 0

        cast_and_crew = {}

        for job in cast_crew_jobs:
            # print job
            # print job.strip()

            # just getting rid of some ugly whitespace around some job types
            job = job.strip()

            # skips a couple empty lines that desynchronize jobs and cast/crew
            if not job:
                continue

            # cast has a different xpath, so need to grab that separately
            if 'Cast' != job:
                # table values begin at 1; we want to go through them all
                crew_name_xpath = '//*[@id="fullcredits_content"]/table[%d]/tbody/tr/td[1]/a/text()' % (current_credit + 1)

                # strips trailing newline characters off the crew members' names
                cast_and_crew[job] = [name.strip() if isinstance(name, str) else unicodedata.normalize('NFKD', name.strip()).encode('ascii', 'ignore') for name in cast_crew_tree.xpath(crew_name_xpath)]

            else:
                cast_name_xpath = '//*[@id="fullcredits_content"]/table[3]/tr/td/a/span/text()'

                cast_and_crew[job] = [name.strip() if isinstance(name, str) else unicodedata.normalize('NFKD', name.strip()).encode('ascii', 'ignore') for name in cast_crew_tree.xpath(cast_name_xpath)]

            # increments to the next job
            current_credit += 1

        # print cast_and_crew['Cast']
        return cast_and_crew



