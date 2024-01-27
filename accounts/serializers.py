from rest_framework import serializers
from auth_system.models import CustomUser
from core.errors import APIError, Error


class UserRegistrationSerializer(serializers.Serializer):
    """
    Summary of the registration
    """
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    dob = serializers.DateField()
    gender = serializers.CharField(max_length=10)
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    confirm_password = serializers.CharField(write_only=True, style={'input_type': 'password'})


    def validate(self, data):
        """
        Summary of the registration
        """
        # Ensure the two password fields match
        if data.get('password') != data.get('confirm_password'):
            raise APIError(Error.GENRAL_ERROR, extra=[f"Passwords do not match."])

        # You can add more validation logic here if needed
        return data

    def create(self, validated_data):
        # Create and return a new User instance with the validated data

        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            dob=validated_data['dob'],
            gender=validated_data['gender'],
            password=validated_data['password']
        )
        return user
