from rest_framework.permissions import BasePermission
from account.models import CustomUser


class IsMuseumAdmin(BasePermission):
    """
    The request is authenticated as a museum admin
    """

    def has_permission(self, request, view):
        return bool(
            request.user.is_authenticated and
            request.user.role == CustomUser.Museum_Admin
        )