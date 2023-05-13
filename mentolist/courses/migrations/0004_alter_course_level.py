# Generated by Django 4.2.1 on 2023-05-13 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_rename_name_category_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='level',
            field=models.CharField(choices=[('HIG', 'Высокий'), ('AVG', 'Средний'), ('LOW', 'Низкий')], default='LOW', max_length=3, verbose_name='Уровень сложности курса'),
        ),
    ]