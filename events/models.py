from django.db import models
from django.contrib.auth import get_user_model
from django.utils.timezone import now

User = get_user_model()


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_time = models.DateTimeField()
    location = models.CharField(max_length=255)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    capacity = models.PositiveIntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    attendee_count = models.IntegerField(default=0)


    def clean(self):
        from django.core.exceptions import ValidationError
        if self.date_time < now():
            raise ValidationError('The event date and time cannot be in the past check the date and try again.')
        
        
    def __str__(self):
        return self.organizer
    

class Attendee(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='attendees')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_waitlisted = models.BooleanField(default=False)
# Create your models here.
