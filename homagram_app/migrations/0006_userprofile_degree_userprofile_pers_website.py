# Generated by Django 5.0.6 on 2024-05-30 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homagram_app', '0005_alter_userprofile_about_facts_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='degree',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='pers_website',
            field=models.URLField(blank=True, null=True),
        ),
    ]