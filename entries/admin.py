from django.contrib import admin
from .models import Entry, Category, Profile

admin.site.register(Entry)
admin.site.register(Category)
admin.site.register(Profile)