from rest_framework import serializers
from .models import ContactMessage

class SendMessageSerializer(serializers.Serializer):
    class Meta:
        model = ContactMessage
        fields = "__all__"
        

