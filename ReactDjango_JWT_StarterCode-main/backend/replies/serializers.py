from rest_framework import serializers
from .models import Reply

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['text', 'comment', 'user_id']
        depth = 1

comment = serializers.IntegerField(write_only=True)  
user_id = serializers.IntegerField(write_only=True)  