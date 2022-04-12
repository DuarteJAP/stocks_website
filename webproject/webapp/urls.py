from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('resources/',views.ResourcesView.as_view(),name='resources'),
]
