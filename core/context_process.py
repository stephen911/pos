# context_processors.py

from .models import Merchant, RelationshipManager, Terminal, DeviceInfo, Monitor
from django.utils import timezone







def custom_context(request):
    # Retrieve the required data
    terminals = Terminal.objects.all()
    devices = DeviceInfo.objects.all().count()
    unique = Terminal.objects.values('device_info_id').distinct().count()
    totalNoTerminals = terminals.count()

    assigned_devices = devices - unique
    totalNoMerchant = Merchant.objects.all().count()
    totalNoRms = RelationshipManager.objects.all().count()
    totalNoDevices = DeviceInfo.objects.all().count()
    totalNoMonitors = Monitor.objects.all().count()
    totalNoActiveDevices = DeviceInfo.objects.filter(status='active').count()
    totalNoInactiveDevices = DeviceInfo.objects.filter(status='inactive').count()
    current_datetime = timezone.now()
    date = current_datetime.strftime('%d %b, %Y')  # e.g., "23 Apr, 2024"
    time = current_datetime.strftime('%I:%M%p')

    
    
    

    # Create the context dictionary
    context = {
        # 'terminals': terminals,
        'totalNoTerminals': totalNoTerminals,
        'totalNoMerchant': totalNoMerchant,
        'totalNoRms': totalNoRms,
        'totalNoDevices': totalNoDevices,
        'totalNoMonitors': totalNoMonitors,
        'totalNoActiveDevices': totalNoActiveDevices,
        'totalNoInactiveDevices': totalNoInactiveDevices,
        'assignedDevices': unique,
        'unique': assigned_devices,
        'date': date,
        'time': time,
        
    }
    
    # Return the context dictionary
    return context
