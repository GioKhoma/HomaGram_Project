# Generated by Django 5.0.6 on 2024-05-27 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homagram_app', '0006_socialmedialink_profile_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='socialmedialink',
            name='profile_photo',
        ),
        migrations.AddField(
            model_name='socialmedialink',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='resumes/'),
        ),
    ]