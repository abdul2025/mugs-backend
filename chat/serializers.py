from rest_framework import serializers
from .models import Room, Message
from auth_system.models import CustomUser



class UserSerializer(serializers.ModelSerializer):
    """
        Summary description
    """
    class Meta:
        """
        Summary description
        """
        model = CustomUser
        fields = ['id', 'username']

class MessageSerializer(serializers.ModelSerializer):
    """
        Summary description
    """
    user = UserSerializer()

    class Meta:
        """
        Summary description
        """
        model = Message
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    """
        Summary description
    """
    class Meta:
        """
        Summary description
        """
        model = Room
        fields = '__all__'