from django.db import models


class Arthur(models.Model):
    born = models.DateTimeField()
    died = models.DateTimeField()
    moved_to_la = models.DateTimeField()
    married_year = models.DateTimeField()
    crew_member = models.OneToOneField('CrewMember')
    arthur_image = models.ImageField(upload_to='arthur', blank=True, null=True)

    def __unicode__(self):
        return self.crew_member.name


class ArthurChild(models.Model):
    name = models.CharField(max_length=100)
    born = models.DateTimeField()
    died = models.DateTimeField()
    father = models.ForeignKey('Arthur')
    # married = models.DateTimeField
    # divorced = models.DateTimeField()

    def __unicode__(self):
        return self.name


# class ArthurGrandchild(models.Model):
#     name = models.CharField(max_length=100)
#     born = models.DateTimeField()
#     grandfather = models.ForeignKey('Arthur')


class Movie(models.Model):
    title = models.CharField(max_length=255)
    year_released = models.DateTimeField()
    genre = models.CharField(max_length=100, blank=True, null=True)
    # studio = models.CharField(max_length=255, blank=True, null=True)
    poster = models.ImageField(upload_to='posters', blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    arthur = models.ForeignKey('Arthur')

    def __unicode__(self):
        return self.title, self.year_released


class CastMember(models.Model):
    name = models.CharField(max_length=120)
    # character = models.CharField(max_length=120, null=True, blank=True)
    movie = models.ManyToManyField('Movie')

    def __unicode__(self):
        return self.name, self.character


class CrewMember(models.model):
    name = models.CharField(max_length=120)
    job = models.CharField(max_length=120)
    movie = models.ManyToManyField('Movie')

    def __unicode__(self):
        return self.name, self.job