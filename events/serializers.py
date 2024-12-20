from rest_framework import serializers
from .models import Event, Attendee



class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

    def validate_date_time(self, value):
        from django.utils.timezone import now
        if value < now():
            raise serializers.ValidationError('Event date must be in the future it cannot be in the past')
        return value
    
    def validate_capacity(self, value):
        if value <= 0:
            raise serializers.ValidationError('Event cannot have negative guests or attendees')
        return value

class Attendee(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        fields = '__all__'