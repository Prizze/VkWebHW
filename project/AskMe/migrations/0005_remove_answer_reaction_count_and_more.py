# Generated by Django 5.1.2 on 2024-11-12 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AskMe', '0004_remove_answer_like_dislike_diff_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='reaction_count',
        ),
        migrations.RemoveField(
            model_name='question',
            name='reaction_count',
        ),
    ]
