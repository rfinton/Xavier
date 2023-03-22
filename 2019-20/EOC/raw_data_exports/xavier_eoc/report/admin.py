from django.contrib import admin
from .models import Campaign, Config, Contact, Event, InboundDetail, Inbound, OutboundSchedule, Outbound, Program, ResponseType, ServiceType, Data

admin.site.register(Campaign)
admin.site.register(Config)
admin.site.register(Contact)
admin.site.register(Event)
admin.site.register(InboundDetail)
admin.site.register(Inbound)
admin.site.register(OutboundSchedule)
admin.site.register(Outbound)
admin.site.register(Program)
admin.site.register(ResponseType)
admin.site.register(ServiceType)
admin.site.register(Data)