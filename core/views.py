from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from .models import Task
from .serializers import TaskSerializer
from datetime import datetime, timedelta
# Create your views here.



class TasksViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class LastDaysCompletedTask(ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        date = datetime.now() - timedelta(days=7)
        return Task.objects.filter(created_at__gte=date, completed=True)
