from django.db import models


class Arthur(models.Model):
    born = models.IntegerField()
    died = models.IntegerField()
    moved_to_la = models.IntegerField()
    married_year = models.IntegerField()
    crew_member = models.OneToOneField('CrewMember', null=True, blank=True)
    arthur_image = models.ImageField(upload_to='arthur', blank=True, null=True)

    def __unicode__(self):
        if self.crew_member:
            return "%s" % self.crew_member.name
        else:
            return "Arthur Piantadosi, born in New York in %d" % self.born

    class Meta:
        verbose_name = 'Arthur'
        verbose_name_plural = 'Arthur'


# class ArthurChild(models.Model):
#     name = models.CharField(max_length=100)
#     born = models.IntegerField()
#     died = models.IntegerField()
#     father = models.ForeignKey('Arthur')
#     # married = models.DateTimeField
#     # divorced = models.DateTimeField()

#     def __unicode__(self):
#         return self.name


class ArthurGrandchild(models.Model):
    name = models.CharField(max_length=100)
    born = models.IntegerField()
    grandfather = models.ForeignKey('Arthur')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Grandchild'
        verbose_name_plural = 'Grandchildren'


class Movie(models.Model):
    title = models.CharField(max_length=255)
    year_released = models.IntegerField()
    genre = models.CharField(max_length=100, blank=True, null=True)
    # studio = models.CharField(max_length=255, blank=True, null=True)
    poster = models.ImageField(upload_to='posters', blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    # arthur = models.ForeignKey('Arthur')

    def __unicode__(self):
        return self.title #, '%s' % str(self.year_released)


class CastMember(models.Model):
    name = models.CharField(max_length=120)
    # character = models.CharField(max_length=120, null=True, blank=True)
    movie = models.ManyToManyField('Movie')

    # class Meta:
    #     unique_together = ['name', 'movie']

    # def __iter__(self):
    #     return [
    #         self.name
    #         # self.movie.title
    #     ]

    def __unicode__(self):
        return self.name, self.movie_set.movie #, self.character


class CrewMember(models.Model):
    name = models.CharField(max_length=120)
    # job_category = models.CharField(max_length=120)
    job_title = models.CharField(max_length=200, blank=True, null=True)
    movie = models.ManyToManyField('Movie')

    # class Meta:
    #     unique_together = ['name', 'job_title', 'movie']

    # def __iter__(self):
    #     return [
    #         self.name,
    #         self.job_title,
    #         # self.movie.title
    #     ]

    def __unicode__(self):
        return "%s, %s" % (self.name, self.job_title)