from django.db import models

# Create your models here.

#Definir el modelo con sus campos
class Task(models.Model):

    CATEGORIES = (
        ('0', 'Personal'),
        ('1', 'Trabajo'),
        ('2', 'Estudio'),
        ('3', 'Otros')
    )

    title = models.CharField(max_length=225)
    description = models.TextField()
    #Para especificar que un campo no es obligatorio blank=True, null=True
    category = models.CharField(max_length=15, choices=CATEGORIES)
    deadline = models.DateTimeField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} {self.completed}'
