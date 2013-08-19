from django.contrib import admin
from ads.models import Advertisment

class AdvertismentAdmin(admin.ModelAdmin):
	fields = ['message','name']

admin.site.register(Advertisment, AdvertismentAdmin)
