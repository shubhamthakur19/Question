from django.contrib import admin
from .models import Question, Question_set, Options
# Register your models here.
admin.site.register(Question_set)
admin.site.register(Question)
admin.site.register(Options)
