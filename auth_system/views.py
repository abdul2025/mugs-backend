from rest_framework_simplejwt.views import TokenObtainPairView
from django.conf import settings
from django.middleware import csrf
from .serializers import MyTokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

class MyTokenObtainPairView(TokenObtainPairView):
    """_summary_

    """
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        """_summary_
            - create token for the requester and add it as cookie
        """

        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:

            response.set_cookie(
                settings.SIMPLE_JWT['AUTH_COOKIE'],  # key
                response.data["access"],  # value
                expires=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                samesite='None'
            )

        return response


class LogOutView(APIView):
    """_summary_

    """

    def get(self, request):
        """_summary_

        """
        response = Response(data={'status': 'success'})
        # validate the requester cookies has token
        raw_token = request.COOKIES.get(settings.SIMPLE_JWT['AUTH_COOKIE']) or None

        if raw_token is None:
            response = Response(data={'status': 'Already logged out'})

        if response.status_code == 200:
            response.set_cookie(
            key=settings.SIMPLE_JWT['AUTH_COOKIE'],
            expires='Thu, 01 Jan 1970 00:00:00 GMT',
            secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
            httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
            samesite='None'
        )

        return response
