# Generated by Django 4.1.3 on 2023-07-02 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_remove_session_lastcard_session_arquitectura_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='answer1',
            field=models.CharField(choices=[('opt1', 'opt1'), ('opt2', 'opt2'), ('opt3', 'opt3'), ('opt4', 'opt4')], default=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='session',
            name='answer2',
            field=models.CharField(choices=[('opt1', 'opt1'), ('opt2', 'opt2'), ('opt3', 'opt3'), ('opt4', 'opt4')], default=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='session',
            name='answer3',
            field=models.CharField(choices=[('opt1', 'opt1'), ('opt2', 'opt2'), ('opt3', 'opt3'), ('opt4', 'opt4')], default=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='session',
            name='answer4',
            field=models.CharField(choices=[('opt1', 'opt1'), ('opt2', 'opt2'), ('opt3', 'opt3'), ('opt4', 'opt4')], default=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='session',
            name='answer5',
            field=models.CharField(choices=[('opt1', 'opt1'), ('opt2', 'opt2'), ('opt3', 'opt3'), ('opt4', 'opt4')], default=True, max_length=4, null=True),
        ),
    ]
