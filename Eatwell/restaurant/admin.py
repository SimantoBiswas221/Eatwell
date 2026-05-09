from django.contrib import admin
from .models import Blog

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display=('title','slug','created_on')
    search_fields=['title','content']
admin.site.register(Blog,BlogAdmin)
