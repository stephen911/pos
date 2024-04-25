

from django import forms
from .models import Monitor, RelationshipManager, Merchant, MerchantContactPerson, TerminalLocation, DeviceInfo, Terminal


class TerminalForm(forms.ModelForm):
    class Meta:
        model = Terminal
        fields = '__all__'
        widgets = {
            'terminal_id': forms.TextInput(attrs={'class': 'form-control'}),
            'terminal_name': forms.TextInput(attrs={'class': 'form-control'}),
            'terminal_address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'pos_id': forms.TextInput(attrs={'class': 'form-control'}),
            'service': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
        # merchant = forms.ModelChoiceField(
        # queryset=Merchant.objects.all(),
        # to_field_name='merchant',
        # required=True,  
        # widget=forms.Select(attrs={'class': 'form-control'})
        # )

    # name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    


class MerchantForm(forms.ModelForm):
    class Meta:
        model = Merchant
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'settlement_account': forms.TextInput(attrs={'class': 'form-control'}),
            'bank': forms.TextInput(attrs={'class': 'form-control'}),
            'branch': forms.TextInput(attrs={'class': 'form-control'}),
            # Assuming RelationshipManager and MerchantContactPerson are imported models
            'relationship_manager': forms.Select(attrs={'class': 'form-select rounded-pill mb-3'}),
            'contact_person': forms.Select(attrs={'class': 'form-select rounded-pill mb-3'}),
        }

    
    


class RelationshipManagerForm(forms.ModelForm):
    class Meta:
        model = RelationshipManager
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
    
    


class MerchantContactPersonForm(forms.ModelForm):
    class Meta:
        model = MerchantContactPerson
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }




class DeviceInfoForm(forms.ModelForm):
    class Meta:
        model = DeviceInfo
        fields = '__all__'
        widgets = {
            'device_id': forms.TextInput(attrs={'class': 'form-control'}),
            'device_name': forms.TextInput(attrs={'class': 'form-control'}),
            'serialnumber': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'connectivity': forms.TextInput(attrs={'class': 'form-control'}),
            'sim': forms.TextInput(attrs={'class': 'form-control'}),
        }



class MonitorForm(forms.ModelForm):
    class Meta:
        model = Monitor
        fields = '__all__'
        widgets = {
            'relationship_manager': forms.Select(attrs={'class': 'form-control'}),
            'monitor_id': forms.TextInput(attrs={'class': 'form-control'}),
            'monitor_name': forms.TextInput(attrs={'class': 'form-control'}),
            'monitor_address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            # 'created_at' and 'updated_at' are auto-generated fields, so they are not included in the form
        }
