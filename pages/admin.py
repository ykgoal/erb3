from django.contrib import admin
from .models import Flower
# Register your models here.

class FlowerAdmin(admin.ModelAdmin):
    list_display = 'id', 'name',        
    list_display_links = ('id', 'name')
    list_filter = 'name',
    search_fields = 'name',
    list_per_page = 25

admin.site.register(Flower, FlowerAdmin)
