from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework import generics, status, serializers
from django_filters.rest_framework import DjangoFilterBackend
from .models import PropertyManager, Landlord, CustomUser
from .serializers import PropertyManagerSerializer, LandlordSerializer, CustomUserSerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .permissions import IsAdminUser

# Token View


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class CustomUserCreateAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            custom_user = CustomUser.objects.get(user=request.user)
            serializer = CustomUserSerializer(custom_user)
            return Response(serializer.data)
        except CustomUser.DoesNotExist:
            return Response({"detail": "Custom user not found."}, status=404)


class PropertyManagerListCreateAPIView(generics.ListCreateAPIView):
    queryset = PropertyManager.objects.all()
    serializer_class = PropertyManagerSerializer
    # Add DjangoFilterBackend to enable filtering
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'first_name', 'last_name']


class PropertyManagerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PropertyManager.objects.all()
    serializer_class = PropertyManagerSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_propertymanager(request):
    # Get the requesting user
    user = request.user

    # Filter the Landlord queryset based on the requesting user
    try:
        landlord = PropertyManager.objects.get(user=user)
    except Landlord.DoesNotExist:
        return Response({"message": "Property not found for the user."}, status=status.HTTP_404_NOT_FOUND)

    # Serialize the landlord object
    serializer = PropertyManagerSerializer(landlord)
    return Response(serializer.data)


class LandlordListCreateAPIView(generics.ListCreateAPIView):
    queryset = Landlord.objects.all()
    serializer_class = LandlordSerializer
    # permission_classes = [IsAdminUser]


class LandlordRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Landlord.objects.all()
    serializer_class = LandlordSerializer
