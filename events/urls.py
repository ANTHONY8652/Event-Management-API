from django.urls import path
from .views import EventListCreateAPIView, EventRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('list/', EventListCreateAPIView.as_view(), name='event-list-create'),
    path('retrieve/', EventRetrieveUpdateDestroyAPIView.as_view(), name='event-retrieve-destroy'),
]
