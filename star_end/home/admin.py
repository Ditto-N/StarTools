from django.contrib import admin
from home.models import Tool

# Register your models here.
admin.site.register(Tool, fixtures=['initial_data'])  