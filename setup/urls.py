"""
URL configuration for setup project.

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

from todo.views import index, update_task, add_task, delete_task, update_task_status, get_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('update-task/', update_task, name='update_task'),
    path('update-task-status/', update_task_status, name='update_task_status'),
    path('delete-task/', delete_task, name='delete_task'),
    path('add-task/', add_task, name='add_task'),
    path('get-task/<int:task_id>/', get_task, name='get_task'),
]
