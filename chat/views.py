from rest_framework import generics
from auth_system.models import CustomUser
from .models import Room, Message
from .serializers import RoomSerializer, MessageSerializer
from rest_framework.permissions import IsAuthenticated

class RoomListView(generics.ListCreateAPIView):

    permission_classes = [IsAuthenticated]
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class MessageListView(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        room_name = self.kwargs['room_name']
        return Message.objects.filter(room__name=room_name)

    def perform_create(self, serializer):
        room_name = self.kwargs['room_name']
        room = Room.objects.get(name=room_name)
        serializer.save(room=room, user=self.request.user)