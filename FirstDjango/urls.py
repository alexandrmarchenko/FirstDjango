from django.contrib import admin
from django.urls import path
from MainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
]
