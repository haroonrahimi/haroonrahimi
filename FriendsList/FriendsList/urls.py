"""FriendsList URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from friends import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    path('info/', views.info, name = 'info'),
    path('add_category/', views.add_category, name = 'add_category'),
    path('add_friend/', views.add_friend, name = 'add_friend'),
    path('category_list', views.category_list, name = 'category_list')
]
