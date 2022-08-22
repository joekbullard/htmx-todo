from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date

class User(AbstractUser):
    pass

class TodoList(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'lists'


class Task(models.Model):
    name = models.CharField(max_length=250)
    list = models.ForeignKey(
        TodoList, on_delete=models.CASCADE
    )
    complete = models.BooleanField(default=False)
    date_added = models.DateField(auto_now_add=True)
    date_due = models.DateField(null=False, default=date.today)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'tasks'