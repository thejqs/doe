import csv
from collections import defaultdict

doe_crew_csv = csv.reader(open('doe_crew.csv', 'r'))
# doe_cast_csv = csv.reader(open('doe_cast.csv', 'r'))
# writer = csv.writer(open('counted_cast.csv', 'wb'))
names = defaultdict(int)
jobs = defaultdict(int)
for row in doe_crew_csv:
# for row in doe_cast_csv:
    # print row[1]
    names[row[1]] += 1
    jobs[row[2]] += 1
    # if name in row[2]

# for row in names.items():
#     writer.writerow(row)

for times in sorted(jobs, key=jobs.get, reverse=True):
  print times, jobs[times]

for times in sorted(names, key=names.get, reverse=True):
    print times, names[times]
    