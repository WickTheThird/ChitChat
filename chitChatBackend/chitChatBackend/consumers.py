from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth.decorators import login_required
import json

class MessageConsumer(AsyncWebsocketConsumer):

    @login_required    
    async def connect(self):
        await self.accept()
        
        await self.channel_layer.group_add(
            'message',
            self.channel_name
        )
        
        print("Opened communications")
        
        message = await self.get_all_messages()
        await self.senf(text_data=json.dumps(message))

    @login_required
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            'message',
            self.channel_name
        )
        
        print("Disconnected from Message Cons!", self.channel_name)


    @login_required
    @database_sync_to_async
    def get_all_messages(self):
        
        from chat import models
        messages = models.Message.objects.all.filter(reciever=self.user)
        
        message_serialiser = [
            {
                'content': messages.content,
                'created_at': messages.created_at,
                'sender': messages.sender
            }
        ]
        
        return message_serialiser
