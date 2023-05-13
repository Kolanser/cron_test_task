from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Question, Category


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
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

    def preview_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 100px;">')
    preview_image.short_description = 'Фото к вопросу'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Админка категорий."""
    list_display = (
        'title',
        'description',
        'preview_image',
    )
    search_fields = ('name', 'description', )
    fields = (
        'title',
        'description',
        'image',
        'preview_image',
    )
    readonly_fields = ('preview_image', )

    def preview_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 100px;">')
    preview_image.short_description = 'Фото категории'
