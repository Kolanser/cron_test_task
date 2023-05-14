from rest_framework import filters, mixins, status, viewsets
from .models import OfflineApplication, Question
from .serializers import OfflineApplicationSerializer, QuestionSerializer


class OfflineApplicationViewSet(
    mixins.CreateModelMixin, viewsets.GenericViewSet
):
    """Представление для добавление заявки."""
    queryset = OfflineApplication.objects.all()
    serializer_class = OfflineApplicationSerializer


class QuestionViewSet(
    mixins.ListModelMixin, viewsets.GenericViewSet
):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
