from rest_framework.permissions import BasePermission
from .models import CustomUser


class IsAdminUser(BasePermission):
    """
    Custom permission to only allow admin users.
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            try:
                custom_user = CustomUser.objects.get(user=request.user)
                return custom_user.role == 'admin'
            except CustomUser.DoesNotExist:
                return False
        return False


class IsEditorUser(BasePermission):
    """
    Custom permission to only allow editor users.
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            try:
                custom_user = CustomUser.objects.get(user=request.user)
                return custom_user.role == 'editor'
            except CustomUser.DoesNotExist:
                return False
        return False


class IsViewerUser(BasePermission):
    """
    Custom permission to only allow viewer users.
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            try:
                custom_user = CustomUser.objects.get(user=request.user)
                # Allow only GET, HEAD, OPTIONS requests for viewers
                if request.method in ['GET', 'HEAD', 'OPTIONS']:
                    return custom_user.role == 'viewer'
                else:
                    return False  # Deny other types of requests
            except CustomUser.DoesNotExist:
                return False
        return False


class IsLandlordUser(BasePermission):
    """
    Custom permission to only allow landlord users.
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            try:
                custom_user = CustomUser.objects.get(user=request.user)
                return custom_user.role == 'landlord'
            except CustomUser.DoesNotExist:
                return False
        return False
