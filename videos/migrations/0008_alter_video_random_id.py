# Generated by Django 3.2.10 on 2023-06-10 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0007_alter_video_random_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='random_id',
            field=models.PositiveIntegerField(default=752, unique=True),
        ),
    ]