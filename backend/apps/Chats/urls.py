from django.urls import path
from .views import ThreadCreateAPIView, ThreadDeleteAPIView, ThreadListAPIView, MessageCreateAPIView, \
    MessageDeleteAPIView

urlpatterns = [
    path('threads/create/', ThreadCreateAPIView.as_view(), name='thread_create'), # створення нової Threads
    path('threads/<int:pk>/delete/', ThreadDeleteAPIView.as_view(), name='thread_delete'),# видалення
    path('threads/list/', ThreadListAPIView.as_view(), name='thread_list'), # cписок всіх Threads
    path('messages/create/', MessageCreateAPIView.as_view(), name='message_create'),# створення нового Message
    path('messages/<int:pk>/delete/', MessageDeleteAPIView.as_view(), name='message_delete'), # для видалення Message з вказаним PK
]
