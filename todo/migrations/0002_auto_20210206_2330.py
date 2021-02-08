# Generated by Django 3.1.5 on 2021-02-06 18:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='status',
        ),
        migrations.AddField(
            model_name='tasks',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tasks',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]