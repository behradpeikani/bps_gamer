# Generated by Django 3.2.10 on 2023-06-07 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_tag_random_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='random_id',
            field=models.PositiveIntegerField(default=8578, unique=True),
        ),
    ]
