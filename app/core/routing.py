from django.urls import path
from core.consumers import *

websocket_urlpatterns = [
    path(r'videos/<str:room_name>/', ChatConsumer),
]
