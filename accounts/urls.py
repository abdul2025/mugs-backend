from django.urls import path, include
from .views import RegistrationView


urlpatterns = [
    path('', RegistrationView.as_view(), name='registerView'),
]
