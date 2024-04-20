"""
URL configuration for server_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from rest_framework import routers
from .views import TasksViewSet, LastDaysCompletedTask

#Instancio la clase Router para crear los endpoints necesarios 
#para realizar las operaciones CRUD, en este caso con el modelo Task 
router = routers.DefaultRouter()

router.register(r"tasks", TasksViewSet, basename="tasks")

#Esta es la lista de urls de mi aplicacion core
urlpatterns = [
    #Endpoint para obtener las tareas completas en los ultimos 7 dias
    path('last_seven_days_completed_tasks/', LastDaysCompletedTask.as_view(), name='last_tasks'),
] + router.urls
