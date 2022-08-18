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
    list_display = ('name', 'review_text', 'product', 'date_created', 'approved_reviews')
    list_filter = ('approved_reviews', 'date_created')
    search_fields = ('name', 'email', 'review_text')
    actions = ['approved_reviews']

    def approved_reviews(self, request, queryset):
        queryset.update(approved_reviews=True)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)