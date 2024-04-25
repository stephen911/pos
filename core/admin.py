from django.contrib import admin
from .models import Terminal, Monitor, Activity, DeviceInfo, MerchantContactPerson, TerminalLocation, Merchant, RelationshipManager

# Register your models here.
@admin.register(Terminal)
class TerminalAdmin(admin.ModelAdmin):
    search_fields = ("terminal_name",)

    
@admin.register(Monitor)
class MonitorAdmin(admin.ModelAdmin):

    search_fields = ("monitor_name",)

    
    
@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):

    search_fields = ("status",)

    
    

@admin.register(DeviceInfo)
class DeviceInfoAdmin(admin.ModelAdmin):
    search_fields = ("status",)


@admin.register(MerchantContactPerson)
class MerchantContactPersonAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    
    
    
@admin.register(TerminalLocation)
class TerminalLocationAdmin(admin.ModelAdmin):
    search_fields = ("town",)
    
    

@admin.register(Merchant)
class MerchantAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    
    
@admin.register(RelationshipManager)
class RelationshipManagerAdmin(admin.ModelAdmin):
    search_fields = ("name",)