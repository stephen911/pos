from django.urls import path
from .views import addDevice, addMContactPerson, addMonitor, downloadreportPOS, editDevice, editPos,  home, index, addMerchants, microsoft_login_callback, reportPOS, v, viewDevice, viewMContactPerson, viewMerchants, addPos, viewMonitor, viewPos, addRms, viewPosDetails, viewRms
from allauth.account.views import LogoutView as AllauthLogoutView
from django.contrib.auth.decorators import login_required


urlpatterns = [

    path('', index, name='index'),
    path('dashboard', home, name='home'),
    path('addMerchants', addMerchants, name='addMerchants'),
    path('viewMerchants', viewMerchants, name='viewMerchants'),
    path('addPos', addPos, name='addPos'),
    path('editPos/<int:id>', editPos, name='editPos'),
    path('viewPosDetails/<int:id>', viewPosDetails, name='viewPosDetails'),
    
    
    path('addDevice', addDevice, name='addDevice'),
    path('viewDevice', viewDevice, name='viewDevice'),
    path('editDevice/<int:id>', editDevice, name='editDevice'),
    
    path('addMonitor', addMonitor, name='addMonitor'),
    path('viewMonitor', viewMonitor, name='viewMonitor'),    
    
    path('viewPos', viewPos, name='viewPos'),
    path('reportPos', reportPOS, name='reportPos'),
    path('downloadreportPos', downloadreportPOS, name='downloadreportPos'),
    
    
    path('addRms', addRms, name='addRms'),
    path('addMContactPerson', addMContactPerson, name='addMContactPerson'),
    path('viewMContactPerson', viewMContactPerson, name='viewMContactPerson'),
    
    
    path('viewRms', viewRms, name='viewRms'),
    path('s', v, name='s'),
    
    path('accounts/logout/', login_required(AllauthLogoutView.as_view()), name='account_logout'),
    path('accounts/microsoft/login/callback/', microsoft_login_callback, name='microsoft_login_callback'),
    
    path('s', v, name='s'),
    
    
    
    
]
