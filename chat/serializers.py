from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):

    session_id = serializers.UUIDField(required=True)
    message = serializers.JSONField(required=True)
    username = serializers.CharField(required=False)
    # dialogflow_resp = serializers.JSONField(required=False)
    direction = serializers.CharField(required=True)
    add_time = serializers.DateTimeField(required=False)

    def create(self, validated_data):

        session_id = validated_data.get('session_id')
        message = validated_data.get('message')
        username = validated_data.get('username')
        # dialogflow_resp = validated_data.get('dialogflow_resp')
        direction = validated_data.get('direction')
        add_time = validated_data.get('add_time')

        new_message = Message()
        new_message.session_id = session_id
        new_message.message = message
        new_message.direction = direction

        if username:
            new_message.username = username
        # if dialogflow_resp:
        #     new_message.dialogflow_resp = dialogflow_resp
        if add_time:
            new_message.add_time = add_time

        new_message.save()

        return new_message

    class Meta:
        model = Message
        fields = ('id', 'username', 'session_id', 'message', 'direction', 'add_time')
