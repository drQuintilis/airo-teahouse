from django.shortcuts import render

# Create your views here.

def main_site(request):
    return render(request, 'teahouse/main.html', {})

def about(request):
    return render(request, 'teahouse/about.html', {})