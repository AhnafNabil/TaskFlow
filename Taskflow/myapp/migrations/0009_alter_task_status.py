# Generated by Django 4.2.6 on 2024-01-12 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Ongoing', 'Ongoing'), ('Done', 'Done')], default='ongoing', max_length=10),
        ),
    ]
