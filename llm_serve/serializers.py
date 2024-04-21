from rest_framework import serializers


class LLMInputSerializer(serializers.Serializer):
    messages = serializers.ListField(required=True)
