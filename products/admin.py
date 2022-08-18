from django.contrib import admin
from .models import Product, Category, Review

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'product', 'date_created', 'approve_reviews')
    list_filter = ('approve_reviews', 'date_created')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(approve_reviews=True)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)