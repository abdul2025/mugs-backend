from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.


class RegistrationView(APIView):
    """_summary_

    """

    def post(self, request):
        """_summary_

        """
        print(request.data)


        return Response(data={'date: Success'}, status=201)


