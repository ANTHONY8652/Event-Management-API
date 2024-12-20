from django.urls import path
from .views import UserDetailView, UserListCreateView, UserLoginView, UserLogoutView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user-register'),
    path('<int:pk>/', UserDetailView.as_view(), name='User-detail'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
]