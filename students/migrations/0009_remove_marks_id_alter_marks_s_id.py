# Generated by Django 4.2 on 2023-04-24 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_marks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marks',
            name='id',
        ),
        migrations.AlterField(
            model_name='marks',
            name='s_id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]
