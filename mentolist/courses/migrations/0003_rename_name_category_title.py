# Generated by Django 4.2.1 on 2023-05-13 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_question_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='title',
        ),
    ]
