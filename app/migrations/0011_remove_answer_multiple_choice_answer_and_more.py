# Generated by Django 4.2.11 on 2024-05-12 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_test_max_attempts_question_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='multiple_choice_answer',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='single_choice_answer',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='text_answer',
        ),
        migrations.AddField(
            model_name='answer',
            name='answer_text',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Answer Text'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='is_correct',
            field=models.BooleanField(default=False, verbose_name='Is Correct'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='app.question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.TextField(verbose_name='Question Text'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('text', 'Text'), ('single_choice', 'Single Choice'), ('multiple_choice', 'Multiple Choice')], max_length=20, verbose_name='Question Type'),
        ),
        migrations.AlterField(
            model_name='question',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='app.test'),
        ),
        migrations.AlterField(
            model_name='question',
            name='topic',
            field=models.CharField(max_length=100, verbose_name='Topic'),
        ),
    ]
