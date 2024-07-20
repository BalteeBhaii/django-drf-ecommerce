from django.contrib import admin

from .models import Brand, Product, Category

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Brand)
