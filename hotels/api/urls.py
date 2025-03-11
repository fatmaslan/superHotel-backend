from django.urls import path
from hotels.api import views as api_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView,UserProfileView,ReservationView

urlpatterns = [
    path('rooms/', api_views.RoomsListCreateAPIView.as_view(), name='oda-ekle'),
    path('rooms/<int:pk>/', api_views.RoomsDetailAPIView.as_view(), name='oda-detay'),
    path('available-rooms/', api_views.AvailableRoomsView.as_view(), name="avaible-rooms"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/profile/', UserProfileView.as_view(), name='profile'),
    path('reservations/', ReservationView.as_view(), name='reservations-list'),
]
