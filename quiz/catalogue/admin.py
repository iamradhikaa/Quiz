from django.contrib import admin
# Register your models here.
from .models import Question, Option



admin.site.register([Question,  Option])