from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    OfflineApplicationViewSet,
    QuestionViewSet,
    CourseViewSet,
    CategoryViewSet
)

router = DefaultRouter()


router.register('submit-applications',
                OfflineApplicationViewSet,
                basename='submit-application')
router.register('courses', CourseViewSet, basename='course')
router.register('questions', QuestionViewSet, basename='question')
router.register('categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls)),
]
