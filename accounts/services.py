from .models import UserProfile
from core.errors import APIError, Error

class AccountService:


    @staticmethod
    def create_profile(user):
        """
        Assigning Custom user to a profile
        """
        try:
            # create a profile per the type
            profile = UserProfile(
                user=user,
            )
            profile.save()
        except Exception as exc:
            raise APIError(Error.GENRAL_ERROR, extra=[f"profile already exists with this email: {user.email}"])