# Generated by Django 4.2.1 on 2023-05-14 11:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_alter_course_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfflineApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(help_text='Номер телефона должен быть в формате +7(xxx)xx-xx-xx', max_length=17, validators=[django.core.validators.RegexValidator('^(\\+7\\([0-9]{3}\\)[0-9]{3}-[0-9]{2}-[0-9]{2})$', message='Номер телефона должен быть в формате +7(xxx)xx-xx-xx')], verbose_name='Номер телефона')),
                ('name', models.CharField(max_length=64, verbose_name='Имя')),
            ],
            options={
                'verbose_name': 'Оффлайн-заявка',
                'verbose_name_plural': 'Оффлайн-заявки',
                'ordering': ['id'],
            },
        ),
    ]