from rest_framework import mixins, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import OfflineApplication, Question, Course, Category
from .serializers import (
    OfflineApplicationSerializer,
    QuestionSerializer,
    CourseSerializer,
    CategorySerializer,
    CourseRetrieveSerializer
)
from .filters import CourseFilter


class OfflineApplicationViewSet(mixins.CreateModelMixin,
                                viewsets.GenericViewSet):
    """Добавление оффлайн-заявки."""
    queryset = OfflineApplication.objects.all()
    serializer_class = OfflineApplicationSerializer


class QuestionViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """Получение списка вопросов."""
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    """Получение данных о курсах."""
    queryset = Course.objects.all()
    filter_backends = (DjangoFilterBackend, )
    filterset_class = CourseFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return CourseSerializer
        return CourseRetrieveSerializer


class CategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """Получение данных о категориях."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
