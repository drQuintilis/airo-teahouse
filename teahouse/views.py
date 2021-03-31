from django.shortcuts import render, redirect

from teahouse.forms import ResponseForm
from teahouse.models import MenuItem, ResponseItem

# Create your views here.

def main_site(request):
    return render(request, 'teahouse/main.html', {})

def about(request):
    return render(request, 'teahouse/about.html', {})

def menu(request):
    menu_items = MenuItem.objects.values()
    return render(request, 'teahouse/menu.html', {'menu_items': menu_items})

def reviews(request):
    if request.method == "POST":
        form = ResponseForm(request.POST)
        form.save(commit=True)
        return redirect('reviews')
    else:
        form = ResponseForm()
        reviews_list = ResponseItem.objects.values()
        return render(request, 'teahouse/reviews.html', {
            'reviews': reviews_list,
            'form': form,
        })