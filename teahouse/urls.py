from django.urls import path

from teahouse import views

urlpatterns = [
    path('', views.main_site, name='main_site'),
    path('о-чайной/', views.about, name='about'),
    path('меню/', views.menu, name='menu'),
]