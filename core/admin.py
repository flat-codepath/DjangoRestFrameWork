from django.contrib import admin
from .models import Category, Product


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    model = Category
    fields = ['name']

# admin.site.register(categoryAdmin)
admin.site.register(Category,CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    model= Product
    fields = ['name', 'price','stock_quantity','category','description']


admin.site.register(Product,ProductAdmin)