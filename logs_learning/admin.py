from django.contrib import admin

# Register your models here.

from logs_learning.models import Topic, Entry

admin.site.register(Topic)
admin.site.register(Entry)