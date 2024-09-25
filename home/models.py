from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Task(models.Model):
    taskTitle = models.CharField(max_length=8, unique=True)
    taskDesc = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if not self.taskTitle:
            raise ValidationError('Task title cannot be empty.')

    def save(self, *args, **kwargs):
        self.clean()  # Call the clean method to enforce validation
        super().save(*args, **kwargs)

    def __str__(self):
        return self.taskTitle 