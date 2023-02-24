from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from .models import Thread, Message
from .serializers import ThreadSerializer, MessageSerializer


class ThreadCreateAPIView(generics.CreateAPIView):
    serializer_class = ThreadSerializer

    def create(self, request, *args, **kwargs):
        user1 = request.data.get('user1')
        user2 = request.data.get('user2')
        thread = Thread.objects.filter(participants=user1).filter(participants=user2).first()

        if thread:
            serializer = self.get_serializer(thread)
            return Response(serializer.data)

        return super().create(request, *args, **kwargs)


class ThreadDeleteAPIView(generics.DestroyAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer


class ThreadListAPIView(generics.ListAPIView):
    serializer_class = ThreadSerializer

    def get_queryset(self):
        user = self.request.user
        return Thread.objects.filter(participants=user)


class MessageCreateAPIView(generics.CreateAPIView):
    serializer_class = MessageSerializer


class MessageDeleteAPIView(generics.DestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
