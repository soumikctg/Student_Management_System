# Generated by Django 4.2 on 2023-04-21 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_guardian'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guardians',
            fields=[
                ('guardian_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('relation', models.CharField(max_length=20)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.student')),
            ],
        ),
    ]
