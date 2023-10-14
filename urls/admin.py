from django.contrib import admin
from .models import URL


class URLAdmin(admin.ModelAdmin):
    list_display = ('name', 'shorturl')  # Fields to display in the list view
    list_filter = ('name',)  # Add filters for fields
    search_fields = ('name',)  # Add search functionality
    fieldsets = (
        ('General', {
            'fields': ('name', 'Full_url')
        }),
    )

# You can customize other admin options here, such as list_per_page, list_editable, etc.

admin.site.register(URL, URLAdmin)  # Register the custom admin class
