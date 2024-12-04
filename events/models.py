from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_time = models.DateTimeField()
    location = models.CharField(max_length=255)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    capacity = models.PositiveIntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)


    def clean(self):
        from django.core.exceptions import ValidationError
        if self.date_time < now():
            raise ValidationError('The event date and time cannot be in the past check the date and try again.')
        
    def __str__(self):
        return self.title - self.organizer - self.description - self.date_time
# Create your models here.
