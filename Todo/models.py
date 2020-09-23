from django.db import models

# Create your models here.


class TodoApp(models.Model):
    content = models.TextField()
