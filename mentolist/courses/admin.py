from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Question, Category, Course, OfflineApplication, HIGH, AVERAGE, LOW


class ImageDisplay(admin.ModelAdmin):
    def preview_image(self, obj):
        return mark_safe(
            f'<img src="{obj.image.url}" style="max-height: 100px;">'
        )
    preview_image.short_description = 'Изображение'

    class Meta:
        abstract = True


@admin.register(Question)
class QuestionAdmin(ImageDisplay):
    """Админка вопроса."""
    list_display = (
        'number',
        'text',
        'preview_image',
    )
    search_fields = ('text', )
    fields = (
        'number',
        'text',
        'image',
        'preview_image',
    )
    readonly_fields = ('preview_image', )


@admin.register(Category)
class CategoryAdmin(ImageDisplay):
    """Админка категорий."""
    list_display = (
        'title',
        'description',
        'preview_image',
    )
    search_fields = ('title', 'description', )
    fields = (
        'title',
        'description',
        'image',
        'preview_image',
    )
    readonly_fields = ('preview_image', )


@admin.register(Course)
class CourseAdmin(ImageDisplay):
    """Админка курсов."""
    list_display = (
        'title',
        'category',
        'time',
        'color_level',
        'description',
        'audio',
        'video',
        'preview_image',
        'is_audio_course',
        'is_video_course'
    )
    search_fields = ('title', 'description', )
    list_filter = (
        'category',
        'level',
    )

    def color_level(self, obj):
        level_color = {
            HIGH: 'Tomato',
            AVERAGE: 'Orange',
            LOW: 'SpringGreen'
        }
        return mark_safe(
            (
                '<div style="width:100%%; height:100%%; '
                f'background-color:{level_color[obj.level]};">'
                f'{obj.get_level_display()}</div>'
            )
        )
    color_level.short_description = 'Сложность курса'


@admin.register(OfflineApplication)
class OfflineApplicationAdmin(ImageDisplay):
    """Админка оффлайн-заявок."""
    list_display = ('name', 'phone_number', )
    search_fields = ('name', 'phone_number', )