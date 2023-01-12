from django.contrib import admin
from .models import Tag, Breed, Pet

admin.site.register(Tag)
admin.site.register(Breed)
admin.site.register(Pet)