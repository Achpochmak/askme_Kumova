# Generated by Django 4.2.11 on 2024-05-13 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_remove_questionresult_selected_answers_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionresult',
            name='selected_answers',
        ),
        migrations.AddField(
            model_name='questionresult',
            name='selected_answers',
            field=models.ManyToManyField(to='app.answer'),
        ),
    ]
