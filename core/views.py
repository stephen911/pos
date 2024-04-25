import os
from django.shortcuts import get_object_or_404, render

from core.forms import DeviceInfoForm, MerchantContactPersonForm, MonitorForm, TerminalForm, MerchantForm, RelationshipManagerForm
from django.contrib import messages
from .models import DeviceInfo, Merchant, MerchantContactPerson, Monitor, RelationshipManager, Terminal
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
import requests

from django.contrib.auth.hashers import make_password
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login

import csv
from django.http import HttpResponse

from django.contrib.auth.models import User

def index(request):
    return render(request, 'auth-signin-cover.html')


def home(request):
    context = {}
    terminals = Terminal.objects.all()
    context['terminals'] = terminals
    return render(request, 'index.html', context=context)



def addPos(request):
    if request.method == 'POST':
        form = TerminalForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'POS Added Successfully')
            return render(request, 'addPos.html', {'form': form})
    
    form = TerminalForm()
    context = {}
    context['form'] = form    
    return render(request, 'addPos.html', context=context)




def editPos(request, id):
    terminal_instance = get_object_or_404(Terminal, pk=id)
    
    if request.method == 'POST':
        form = TerminalForm(request.POST, instance=terminal_instance)
        if form.is_valid():
            form.save()
            messages.success(request, 'POS Updated Successfully')
            return render(request, 'editPos.html', {'form': form, "terminal_id": terminal_instance.id})
    else:
        # form = TerminalForm(instance=terminal_instance)
        form = TerminalForm(instance=terminal_instance, initial={'device_info': terminal_instance.device_info})

    context = {'form': form, "terminal_id": terminal_instance.id}
    return render(request, 'editPos.html', context)



def viewPosDetails(request, id):
    terminal_instance = get_object_or_404(Terminal, pk=id)
    context = {'terminal': terminal_instance, "terminal_id": terminal_instance.id}
    return render(request, 'viewPosDetails.html', context)






def viewPos(request):
    terminals = Terminal.objects.all()  # Assuming you have a Terminal model
    # paginator = Paginator(terminal_list, 2)  # Show 10 terminals per page
    # page = request.GET.get('page')
    # try:
    #     terminals = paginator.page(page)
    # except PageNotAnInteger:
    #     # If page is not an integer, deliver first page.
    #     terminals = paginator.page(1)
    # except EmptyPage:
    #     # If page is out of range (e.g. 9999), deliver last page of results.
    #     terminals = paginator.page(paginator.num_pages)

    return render(request, 'viewPos.html', {'terminals': terminals})



def reportPOS(request):
    context = {}
    terminals = Terminal.objects.all()
    context['terminals'] = terminals
    return render(request, 'reportDetails.html', context=context)





def downloadreportPOS(request):
    # Your data queryset
    terminals = Terminal.objects.all()

    # Create a CSV response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="report.csv"'

    # Create a CSV writer
    writer = csv.writer(response)
    # Write header row
    writer.writerow(['Terminal ID', 'Terminal Name', 'Merchant', 'Monitor', 'Relationship Manager', 'Branch', 'Location', 'Device Status'])  # Modify headers as needed

    # Write data rows
    for terminal in terminals:
        device_status = terminal.device_info.status if terminal.device_info else ""
        writer.writerow([terminal.id, terminal.terminal_name, terminal.merchant.name, terminal.monitor.monitor_name, terminal.merchant.relationship_manager, terminal.merchant.branch, terminal.location.town, device_status])  # Modify fields as needed

    return response


def addMerchants(request):
    if request.method == 'POST':
        form = MerchantForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Merchant Added Successfully')
            return render(request, 'addMerchants.html', {'form': form})
    
    form = MerchantForm()
    context = {}
    context['form'] = form  
    return render(request, 'addMerchants.html', context=context)


def viewMerchants(request):
    merchants = Merchant.objects.select_related('relationship_manager').all()
    context = {'merchants': merchants}
    return render(request, 'viewMerchants.html', context=context)




def addRms(request):
    if request.method == 'POST':
        form = RelationshipManagerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'RM Added Successfully')
            return render(request, 'addRms.html', {'form': form})
    
    form = RelationshipManagerForm()
    context = {}
    context['form'] = form  
    return render(request, 'addRms.html', context=context)


def viewRms(request):
    rms = RelationshipManager.objects.all()
    context = {'rms': rms}
    return render(request, 'viewRms.html', context=context)





def addMContactPerson(request):
    if request.method == 'POST':
        form = MerchantContactPersonForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Merchant Contact Person Added Successfully')
            return render(request, 'addMContactPerson.html', {'form': form})
    
    form = MerchantContactPersonForm()
    context = {}
    context['form'] = form  
    return render(request, 'addMContactPerson.html', context=context)


def viewMContactPerson(request):
    
    cm = MerchantContactPerson.objects.all()
    context = {'cms': cm}
    return render(request, 'viewMContactPerson.html', context=context)


def viewDevice(request):
    
    # device_info_instance.terminals.exists()
    
    devices = DeviceInfo.objects.all()
    
    # for device in devices:
    #     assigned = Terminal.objects.filter(device_info=device).exists()

    
        
    context = {'devices': devices}
    return render(request, 'viewDevices.html', context=context)



def addDevice(request):
    
    if request.method == 'POST':
        form = DeviceInfoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Device Added Successfully')
            return render(request, 'addDevice.html', {'form': form})
    
    form = DeviceInfoForm()
    context = {}
    context['form'] = form    
    return render(request, 'addDevice.html', context=context)




def editDevice(request, id):
    device_instance = get_object_or_404(DeviceInfo, pk=id)
    
    if request.method == 'POST':
        form = DeviceInfoForm(request.POST, instance=device_instance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Device Updated Successfully')
            return render(request, 'editDevice.html', {'form': form, "device_id": device_instance.id})
    else:
        form = DeviceInfoForm(instance=device_instance)

    context = {'form': form, "device_id": device_instance.id}
    return render(request, 'editDevice.html', context)




def viewMonitor(request):
    monitors = Monitor.objects.all()
    context = {'monitors': monitors}
    return render(request, 'viewMonitor.html', context=context)



def addMonitor(request):
    
    if request.method == 'POST':
        form = MonitorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Monitor Added Successfully')
            return render(request, 'addMonitor.html', {'form': form})
    
    form = MonitorForm()
    context = {}
    context['form'] = form    
    return render(request, 'addMonitor.html', context=context)
def v(request):
    return render(request, 's.html')




























def microsoft_login_callback(request):
    code = request.GET.get('code')
    state = request.GET.get('state')

    print(code)

    # Exchange the authentication code for an access token
    token_endpoint = 'https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token'.format(
        tenant=os.environ.get('TENANT')
    )

    print("okay", token_endpoint)
    token_data = {
        'client_id': os.environ.get('CLIENT'),
        'client_secret': os.environ.get('CLIENT_SECRET'),
        'code': code,
        'redirect_uri': 'http://127.0.0.1:8000/accounts/microsoft/login/callback/',
        'grant_type': 'authorization_code',
    }

    print("tje", token_data)

    try:
        token_response = requests.post(token_endpoint, data=token_data)
        token_response_data = token_response.json()
        access_token = token_response_data.get('access_token')

        # Retrieve user information from Microsoft Graph API
        graph_endpoint = 'https://graph.microsoft.com/v1.0/me'
        headers = {
            'Authorization': 'Bearer {0}'.format(access_token)
        }
        response = requests.get(graph_endpoint, headers=headers)
        user_data = response.json()

        print("user_data", user_data)


        # print(user_data)

        upn = user_data.get('userPrincipalName').lower().split("@")[0]
        display_name = user_data.get('displayName')
        email = user_data.get('mail')
        print(email)

        # Check if the user already exists in the database
        if not User.objects.filter(username=upn).exists():
            # print("im here", upn)
            # Create a new user record
            password = make_password("Omnibsic123")
            user = User(username=upn, first_name=display_name, email=email, password=password)  # Set password to None for external authentication
            # user.first_name = display_name  # Optionally set other user attributes
            user.save()


        # print(request)

        # user = authenticate(request, microsoft_user_data=user_data)
        # print(upn.lower().split("@")[0])
        user = authenticate(username=upn, password="Omnibsic123")
        print("good", user)
        if user:
            login(request, user)
            # Redirect the user to the desired next page or a default page
            next_page = request.GET.get('next', '/')  # Get the next page from the query parameters
            return redirect("dashboard")
        else:
            # Handle authentication failure (e.g., user not found)
            return redirect('home')  # Redirect to login page with appropriate error message
    except requests.HTTPError as e:
        # Handle HTTP errors (e.g., 400 Bad Request)
        print("HTTP Error:", e.response.status_code, e.response.text)
    except requests.RequestException as e:
        # Handle other request errors
        print("Request Error:", e)

        
    return redirect('home')