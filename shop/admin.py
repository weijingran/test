from django.contrib import admin
from .models import Tag, Product, Interaction

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'display_image')  # Add 'display_image'
    list_filter = ('category',)
    list_filter = ('category',)
    search_fields = ('name', 'tags__name')
    filter_horizontal = ('tags',)
    # ADDED fields for the edit form
    fields = ('name', 'description', 'category', 'price', 'stock', 'tags', 'image')  # Add 'image' here

    def display_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])
    display_tags.short_description = 'Tags'

    def display_image(self, obj):  # Method to display the image in the list view
        if obj.image:
            return f'<img src="{obj.image.url}" width="100" height="100" />'  # Display image
        return "No Image"

    display_image.short_description = 'Product Image'
    display_image.allow_tags = True  # This allows HTML to be rendered in the list view

@admin.register(Interaction)
class InteractionAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'action', 'rating', 'created_at')
    list_filter = ('action', 'created_at')
    search_fields = ('user__username', 'product__name')
    list_select_related = ('user', 'product')