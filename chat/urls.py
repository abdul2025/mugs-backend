from django.urls import path
from .views import RoomListView, MessageListView

urlpatterns = [
    path('rooms/', RoomListView.as_view(), name='room-list'),
    path('rooms/<str:room_name>/messages/', MessageListView.as_view(), name='message-list'),
]