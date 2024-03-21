from django.contrib import admin

from user.models import UserProfile

class PageAdmin(admin.ModelAdmin):

     list_display = ('title','category', 'url')

admin.site.register(UserProfile)
