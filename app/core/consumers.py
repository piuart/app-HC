import json
import logging
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sessions.models import Session
from django.db import transaction
from datetime import datetime
from core.youtube.models import *


class ChatConsumer(AsyncWebsocketConsumer, LoginRequiredMixin):
    async def connect(self):
        self.user = self.scope['user']
        # self.scope["session"].session_key
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        try:
            data = {'status': False, 'type': 'chat_message'}
            text_data_json = json.loads(text_data)
            consultar = text_data_json['consultar']
            if consultar:
                fechaactual = datetime.now().date()
                hora = datetime.now().time()
                horamin = "{}:00".format(datetime.now().strftime('%H:%M'))
                print(horamin)
                lista = ListaReproduccion.objects.filter(fecha_subida=fechaactual, hora_subida__icontains=horamin, visto=False).exists()
                if lista:
                    video = ListaReproduccion.objects.filter(fecha_subida=fechaactual, hora_subida__icontains=horamin, visto=False).first()
                    video.visto = True
                    video.save()
                    data['status'] = True
                    data['nombre'] = video.nombre
                    data['link_promo'] = video.link_promo
                    data['idvideo'] = video.idvideo
                    data["hora"] = datetime.now().time().strftime("%H:%M")
                else:
                    data['status'] = False
        except Exception as ex:
            print(ex)

        # Send message to room group
        await self.channel_layer.group_send(self.room_group_name, data)

    # Receive message from room group
    async def chat_message(self, event):
        status = event['status']
        # Send message to WebSocket
        await self.send(text_data=json.dumps(event))
