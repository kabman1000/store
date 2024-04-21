from django.contrib import admin
from .models import Category, Product, SubCategory




@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'inventory', 'code', 'price',
                    'in_stock', 'created','total_value']
    list_filter = ['in_stock', 'is_active']
    list_editable = ['price', 'in_stock','total_value']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['code']


@admin.register(SubCategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display=['name','categories']

