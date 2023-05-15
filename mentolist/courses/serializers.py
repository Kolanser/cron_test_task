from rest_framework import serializers
from .models import OfflineApplication, Question, Course, Category


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


class CourseSerializer(serializers.ModelSerializer):
    """Сериализатор для списка курсов."""
    level = serializers.CharField(
        source='get_level_display'
    )

    class Meta:
        model = Course
        fields = (
            'id',
            'category',
            'title',
            'image',
            'level',
            'is_audio_course',
            'is_video_course'
        )


class CourseRetrieveSerializer(serializers.ModelSerializer):
    """Сериализатор отдельного курса."""
    class Meta:
        model = Course
        fields = (
            'title',
            'image',
            'description',
            'time',
            'audio',
            'video',
            'is_audio_course',
            'is_video_course'
        )


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор категорий."""
    class Meta:
        model = Category
        fields = ('id', 'title', 'description', 'image')
