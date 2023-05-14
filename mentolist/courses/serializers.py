from rest_framework import serializers
from .models import OfflineApplication, Question


class OfflineApplicationSerializer(serializers.ModelSerializer):
    """Сериализатор оффлайн-заявки."""
    class Meta:
        model = OfflineApplication
        fields = ('phone_number', 'name')


class QuestionSerializer(serializers.ModelSerializer):
    """Сериализатор вопросов."""
    class Meta:
        model = Question
        fields = ('number', 'text', 'image', )