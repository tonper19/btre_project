from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "city", "is_published", "price", "list_date", "realtor")
    list_display_links = ("id", "title")
    list_filter = ("realtor", "city")
    list_editable = ("is_published", "realtor")
    search_fields = ("title", "description", "price", "address", "city", "state", "bedrooms", "bathrooms")
    list_per_page = 5

admin.site.register(Listing, ListingAdmin)