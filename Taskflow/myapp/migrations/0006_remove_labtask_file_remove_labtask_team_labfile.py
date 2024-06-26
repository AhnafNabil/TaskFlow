# Generated by Django 4.2.6 on 2024-01-10 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_remove_labtask_team_labtask_team'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='labtask',
            name='file',
        ),
        migrations.RemoveField(
            model_name='labtask',
            name='team',
        ),
        migrations.CreateModel(
            name='LabFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('lab_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='myapp.labtask')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lab_files', to='myapp.projectroom')),
            ],
        ),
    ]
