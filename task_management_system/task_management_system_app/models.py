from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)


class Task(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    # priority = models.IntegerField(default=1)
    STATUS_CHOICES = [
        ('to_do', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='to_do')
    description = models.TextField(default='')
    location = models.CharField(max_length=255, default='')
    organizer = models.CharField(max_length=100, default='')


    