# Generated by Django 3.2.10 on 2023-06-03 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_tag_random_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='publish', max_length=100),
        ),
        migrations.AlterField(
            model_name='article',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='random_id',
            field=models.PositiveIntegerField(default=2910, unique=True),
        ),
    ]
