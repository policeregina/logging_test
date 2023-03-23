from django.contrib import admin
from .models import Product, Order


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    list_filter = ('price', 'name')
    search_fields = ('name', 'price__name')


admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
