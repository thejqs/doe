import django
import sys, os
import csv
from collections import defaultdict

sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

django.setup()
from main.models import Arthur, Movie, CastMember, CrewMember

doe_crew_csv = csv.reader(open('doe_crew.csv', 'r'))
# doe_cast_csv = csv.reader(open('doe_cast.csv', 'r'))
# writer = csv.writer(open('counted_cast.csv', 'wb'))

names = defaultdict(int)
jobs = defaultdict(int)
# movies_total = defaultdict(int)

crew_dict = defaultdict(set)

movies = defaultdict(set)

for row in doe_crew_csv:
# for row in doe_cast_csv:
    # print row[1]
    crew_object = CrewMember.objects.get(id=row[0])

    for movie in crew_object.movie.all():
        movies[row[1]].add(movie.title)

    names[row[1]] += 1
    jobs[row[2]] += 1


    crew_dict[row[1]].add(row[2])

# print len(names)
# print len(jobs)

for name in sorted(names, key=names.get, reverse=True):
    # print name, names[name], ", ".join(crew_dict[name])
    print name, len(movies[name]), ", ".join(movies[name]), ", ".join(crew_dict[name])
    # row = name, names[name], ", ".join(movies[name])

    # writer.writerow(row)
