from django.contrib import admin
from app.models import Musician, MusicGenre, Product, Category

# Register your models here.
admin.site.register(Musician)
admin.site.register(MusicGenre)
admin.site.register(Category)
admin.site.register(Product)

