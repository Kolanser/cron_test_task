from django.db import models
from django.core.validators import MinValueValidator, RegexValidator
from django.contrib import admin

HIGH = 'HIG'
AVERAGE = 'AVG'
LOW = 'LOW'


class Question(models.Model):
    """Модель для вопросов."""
    number = models.IntegerField(
        'Порядковый номер вопроса',
        validators=[
            MinValueValidator(
                limit_value=1,
                message='Номер вопроса не может быть меньше 1'
            )
        ],
        unique=True
    )
    text = models.TextField(
        'Текст вопроса',
        unique=True
    )
    image = models.ImageField(
        'Фото к вопросу',
        upload_to='courses/questions/'
    )

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ['id', ]

    def __str__(self):
        return self.text


class Category(models.Model):
    """Модель категорий вопросов."""
    title = models.CharField(
        'Название категории',
        max_length=64,
        unique=True
    )
    description = models.TextField(
        'Описание категории',
        max_length=1024
    )
    image = models.ImageField(
        'Фото категории',
        upload_to='courses/categories/'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Course(models.Model):
    """Модель курсов."""
    LEVEL_CHOICES = [
        (HIGH, 'Высокий'),
        (AVERAGE, 'Средний'),
        (LOW, 'Низкий')
    ]
    category = models.ForeignKey(
        'Category',
        verbose_name='Категория',
        on_delete=models.CASCADE,
        related_name='courses'
    )
    title = models.CharField(
        'Название курса',
        max_length=64,
        unique=True
    )
    time = models.CharField(
        'Время прохождения курса',
        max_length=64
    )
    image = models.ImageField(
        'Фото к курсу',
        upload_to='courses/courses/'
    )
    level = models.CharField(
        'Уровень сложности курса',
        max_length=3,
        choices=LEVEL_CHOICES,
        default=LOW,
    )
    description = models.TextField(
        'Описание курса',
        max_length=2048
    )
    audio = models.FileField(
        'Аудио к курсу',
        upload_to='courses/courses/',
        blank=True,

    )
    video = models.URLField(
        'Видео',
        help_text='Ссылка на видео',
        blank=True
    )

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['id', 'title',]

    @property
    @admin.display(description="Тип курса аудио?")
    def is_audio_course(self):
        return bool(self.video)

    @property
    @admin.display(description="Тип курса видео?")
    def is_video_course(self):
        return bool(self.video)

    def __str__(self):
        return self.title


class OfflineApplication(models.Model):
    """Модель оффлайн-заявок."""
    message_help = 'Номер телефона должен быть в формате +7(xxx)xx-xx-xx'
    phone_number = models.CharField(
        'Номер телефона',
        max_length=17,
        validators=[
            RegexValidator(
                r'^(\+7\([0-9]{3}\)[0-9]{3}-[0-9]{2}-[0-9]{2})$',
                message=message_help,
            )
        ],
        help_text=message_help
    )
    name = models.CharField(
        'Имя',
        max_length=64,
    )

    class Meta:
        verbose_name = 'Оффлайн-заявка'
        verbose_name_plural = 'Оффлайн-заявки'
        ordering = ['id', ]

    def __str__(self):
        return f'{self.name} - {self.phone_number}'
