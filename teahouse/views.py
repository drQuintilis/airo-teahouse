from django.shortcuts import render
from teahouse.models import MenuItem

# Create your views here.

def main_site(request):
    return render(request, 'teahouse/main.html', {})

def about(request):
    return render(request, 'teahouse/about.html', {})

def menu(request):
    menu_items = MenuItem.objects.values()
    return render(request, 'teahouse/menu.html', {'menu_items': menu_items})