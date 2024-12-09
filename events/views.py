from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Event, Attendee
from django.shortcuts import get_object_or_404
from .serializers import EventSerializer
from .permissions import IsOrganizerOrReadOnly


class EventListCreateAPIView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)


class EventRetrieveUpdateDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOrganizerOrReadOnly, IsOrganizerOrReadOnly]


class RegisterForEVentView(generics.GenericAPIView):
    def post(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)
        user = request.user

        if event.attendees_count < event.capacity:
            Attendee.objects.create(event=event, user=user, is_waitlisted=False)
            event.attendees_count += 1
            event.save()
            return Response({'message': 'Registration Successful.'}, status=status.HTTP_201_CREATED)
        
        else:
            Attendee.objects.create(event=event, user=user, is_waitlisted=True)
            return Response({'message': 'Event is full. You have been added to the waitlist.'})

class CancelRegistrationView(generics.GenericAPIView):
    def post(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)
        user = request.user

        attendee = Attendee.objects.filter(event=event, user=user).first()
        if not attendee:
            return Response({'message:' 'You are not registered for this event.'}, status=status.HTTP_400_BAD_REQUEST)
        

        if attendee.is_waitlisted:
            attendee.delete()
            return Response({'message': 'You have been removed fro the waitlist'}, status=status.HTTP_200_OK)
        
        else:
            attendee.delete()
            event.attendees_count -= 1
            event.save()

            waitlisted_user = Attendee.objects.filter(event=event, is_waitlisted=True).first()

            if waitlisted_user:
                waitlisted_user.is_waitlisted = False
                waitlisted_user.save()
                event.attendee_count += 1
                event.save

            return Response({'message': 'Your registration has been cancelled.'}, status=status.HTTP_200_OK)

# Create your views here.
