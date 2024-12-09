from django.urls import path
from .views import EventListCreateAPIView, EventRetrieveUpdateDestroyAPIView, RegisterForEVentView, CancelRegistrationView


urlpatterns = [
    path('list/', EventListCreateAPIView.as_view(), name='event-list-create'),
    path('retrieve/', EventRetrieveUpdateDestroyAPIView.as_view(), name='event-retrieve-destroy'),
    path('register-event/', RegisterForEVentView.as_view(), name='register-event'),
    path('cancel-registration/', CancelRegistrationView.as_view(), name='cancel-registration'),
]
