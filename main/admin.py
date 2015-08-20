from django.contrib import admin
from main.models import Arthur, Movie, CrewMember, CastMember, ArthurGrandchild

# Register your models here.
admin.site.register(Arthur)
admin.site.register(Movie)
admin.site.register(CrewMember)
admin.site.register(CastMember)
admin.site.register(ArthurGrandchild)