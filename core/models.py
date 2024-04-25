from django.db import models

class RelationshipManager(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Merchant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    settlement_account = models.CharField(max_length=100)
    bank = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    relationship_manager = models.ForeignKey(RelationshipManager, on_delete=models.CASCADE)
    contact_person = models.ForeignKey('MerchantContactPerson', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    
class MerchantContactPerson(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

    
class TerminalLocation(models.Model):
    location_id = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    town = models.TextField()
    region = models.CharField(max_length=100)
    zone = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.town

    
    
class DeviceInfo(models.Model):
    choices = [('active', 'Active'), ('inactive', 'Inactive'), ('faulty', 'Faulty'), ('retrieved', 'Retrieved'), ('deployed', 'Deployed'), ]
    device_name = models.CharField(max_length=100)
    serialnumber = models.TextField()
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    connectivity = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=choices, default='inactive')
    sim = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def get_assignment_status(self):
        assigned = Terminal.objects.filter(device_info_id=self.id).exists()
        return assigned
    
    
    def __str__(self):
        assigned = "Assigned" if self.get_assignment_status() else "Unassigned"
        return f"{self.device_name} - {assigned}"


    
class Activity(models.Model):
    device = models.ForeignKey(DeviceInfo, on_delete=models.CASCADE)
    activity_id = models.CharField(max_length=100)
    activity_name = models.CharField(max_length=100)
    activity_address = models.TextField()
    date_deployed = models.DateField()
    last_transaction = models.DateField()
    status = models.CharField(max_length=20)
    period = models.CharField(max_length=20)
    retrieved = models.BooleanField(default=False)
    date_retrieved = models.DateField()
    faulty = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    
    def __str__(self):
        return self.device

    
    

    
class Monitor(models.Model):
    choices = [('zone 1', 'Zone 1'), ('zone 2', 'Zone 2'), ('zone 3', 'Zone 3'),]
    monitor_name = models.CharField(max_length=100)
    monitor_address = models.TextField()
    zone = models.CharField(max_length=20, choices=choices, default="zone1")
    relationship_manager = models.ForeignKey(RelationshipManager, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.monitor_name

    
    



class Terminal(models.Model):
    # choices = [('active', 'Active'), ('inactive', 'Inactive'), ('faulty', 'Faulty'), ('retrieved', 'Retrieved'), ('deployed', 'Deployed'), ]
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    terminal_name = models.CharField(max_length=100)
    terminal_address = models.TextField()
    device_info = models.ForeignKey(DeviceInfo, on_delete=models.CASCADE)
    location = models.ForeignKey(TerminalLocation, on_delete=models.CASCADE)
    # status = models.CharField(max_length=20, choices=choices, default='inactive')
    # Activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE)
    service = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.terminal_name
