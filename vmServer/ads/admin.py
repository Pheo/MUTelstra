from django.contrib import admin
from ads.models import Advertisment, Advertiser, Authentication, AdLocation, Weather, Location, TrivialWeather 

admin.site.register(Advertisment)
admin.site.register(Advertiser)
admin.site.register(Authentication)
admin.site.register(AdLocation)
admin.site.register(Weather)
admin.site.register(Location)
admin.site.register(TrivialWeather)
