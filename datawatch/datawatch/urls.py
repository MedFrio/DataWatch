"""
URL configuration for datawatch project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from datawatch.datawatch import views

urlpatterns = [
    path('admin/', admin.site.urls),path("upload/", views.upload_file, name="upload"),path("", views.accueil, name="accueil"),path('suivi_ticket/', views.suivi_ticket, name='suivi_ticket'),path('check_ticket/<str:ticket_id>/', views.check_ticket_status, name='check_ticket_status'),
]
