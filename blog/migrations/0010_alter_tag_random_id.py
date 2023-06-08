from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20230603_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='random_id',
            field=models.PositiveIntegerField(default=6632, unique=True),
        ),
    ]
