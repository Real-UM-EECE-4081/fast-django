from django.db import models

# Create your models here.

class ToDoItem(models.Model):
    description = models.CharField(max_length=255)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.description}, {self.complete}"

