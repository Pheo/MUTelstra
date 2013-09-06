from django.contrib import admin
from ads.models import Advertisment, Authentication, Disruption, ServiceLocation, Weather, Location 

admin.site.register(Advertisment)
admin.site.register(Authentication)
admin.site.register(Disruption)
admin.site.register(ServiceLocation)
admin.site.register(Weather)
admin.site.register(Location)
