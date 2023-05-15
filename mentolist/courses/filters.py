from django_filters import FilterSet, ChoiceFilter, BooleanFilter
from .models import Course, LEVEL_CHOICES


class CourseFilter(FilterSet):
    """Фильтр для курсов"""
    is_audio_course = BooleanFilter(
        method='filter_is_audio_course',
    )
    is_video_course = BooleanFilter(
        method='filter_is_video_course',
    )
    level = ChoiceFilter(choices=LEVEL_CHOICES)

    def filter_is_audio_course(self, queryset, name, value):
        if value:
            return queryset.exclude(audio='')
        return queryset

    def filter_is_video_course(self, queryset, name, value):
        if value:
            return queryset.exclude(video='')
        return queryset

    class Meta:
        model = Course
        fields = ('level', 'is_audio_course', 'is_video_course')
