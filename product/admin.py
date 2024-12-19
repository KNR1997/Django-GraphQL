from django.contrib import admin

from product.models import Category, Type

# Register your models here.
admin.site.register(Type)
admin.site.register(Category)
