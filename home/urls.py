"""todo_list URL Configuration

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
from django.urls import path,include
from home import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',views.CustomLoginView.as_view(),name='login'),
    path('register/',views.RegisterPage.as_view(),name='register'),
    #path('custom/',views.MyView.as_view(),name='custom'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('', views.home, name='home'),
    path('tasks/<id>', views.tasks, name='tasks'),
    path('delete/<id>',views.delete, name='delete'),
    path('edit/<id>',views.edit, name='edit')
]
