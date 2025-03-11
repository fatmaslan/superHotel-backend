from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework import generics
from hotels.models import Rooms,Reservations
from hotels.api.serializers import RoomsSerializer,ReservationSerializer,RegisterSerializer
from rest_framework.views import APIView
from django.utils.dateparse import parse_date
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

class RoomsListCreateAPIView(generics.ListCreateAPIView):

    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer
    permission_classes = [permissions.AllowAny]


class RoomsDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer
    permission_classes = [permissions.AllowAny]


class AvailableRoomsView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        arrival_date = parse_date(request.data.get("arrivalDate"))
        departure_date  = parse_date(request.data.get("departureDate"))

        if not arrival_date or not departure_date:
            return Response({"error": "Invalid date format"}, status=status.HTTP_400_BAD_REQUEST)
        
        if arrival_date >= departure_date:
            return Response({"error":"Arrival date must be before departure date"},status=status.HTTP_400_BAD_REQUEST)
        
        # uygun odalar
        booked_rooms = Reservations.objects.filter(
        arrival_date__lt=departure_date, 
        departure_date__gt=arrival_date
        ).values_list("rooms_id", flat=True)
        
        available_rooms = Rooms.objects.exclude(id__in=booked_rooms)
        serializer = RoomsSerializer(available_rooms, many=True)

        return Response({"rooms": serializer.data}, status=status.HTTP_200_OK)
    
class ReservationView(APIView):
    queryset = Reservations.objects.all()
    authentication_classes = [JWTAuthentication] 
    permission_classes = [IsAuthenticated]

    def get(self, request):
        
        reservations = Reservations.objects.all()
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)      
    def post(self,request):
        serializer = ReservationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
    
class RegisterView(APIView):

    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")

        if User.objects.filter(email=email).exists():
            return Response({"error": "Email already in use"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, email=email, password=password)
        return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
    
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "id": user.id,
            "email": user.email,
        })