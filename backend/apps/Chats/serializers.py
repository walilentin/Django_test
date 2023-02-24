from rest_framework import serializers
from .models import Thread, Message

# опреділяємо серіалізатори які використовують модель Message
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        #всі поля Message будуть включені в серіалізатор
        fields = '__all__'


class ThreadSerializer(serializers.ModelSerializer):
    last_message = serializers.SerializerMethodField()

    def get_last_message(self, obj):
        try:
            return MessageSerializer(obj.message_set.latest('created')).data
        except Message.DoesNotExist:
            return None

    class Meta:
        model = Thread
        fields = '__all__'
