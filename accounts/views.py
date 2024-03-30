from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer
from .services import AccountService
from core.errors import APIError, Error

# Create your views here.


class RegistrationView(APIView):
    """_summary_
    """

    def post(self, request, *args, **kwargs):
        """_summary_

            - Create Custom user
            - Create Profile
        """
        print(request.data)
        user = None
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            # Save Custom User
            try:
                user = serializer.save()
            except Exception as er:
                raise APIError(Error.GENRAL_ERROR, extra=['Please Use different Email, Email Already Used'])

            # Create a profile
            AccountService.create_profile(user)

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        raise APIError(Error.GENRAL_ERROR, extra=[serializer.errors])



