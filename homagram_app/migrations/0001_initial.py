# Generated by Django 5.0.6 on 2024-05-30 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook_link', models.URLField(blank=True, null=True)),
                ('instagram_link', models.URLField(blank=True, null=True)),
                ('skype_link', models.URLField(blank=True, null=True)),
                ('twitter_link', models.URLField(blank=True, null=True)),
                ('linkedin_link', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField(blank=True, default='Your birth_date: ', null=True)),
                ('age', models.IntegerField(blank=True, default='Your age: ', null=True)),
                ('phone', models.IntegerField(blank=True, null=True, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('title_about_text', models.CharField(blank=True, default='The title of the text about you', max_length=50, null=True)),
                ('about_text', models.CharField(blank=True, default='About you: ', max_length=200, null=True)),
                ('profile_photo', models.ImageField(blank=True, default='img/default_img.jpg', null=True, upload_to='img/profile_img')),
                ('about_facts', models.CharField(blank=True, default='Facts about you: ', max_length=100, null=True)),
                ('happy_clients', models.IntegerField(default=0)),
                ('projects', models.IntegerField(default=0)),
                ('hours_of_support', models.IntegerField(default=0)),
                ('hard_worker', models.IntegerField(default=0)),
                ('location', models.CharField(blank=True, default='Your Location', max_length=40, null=True)),
                ('resume', models.FileField(blank=True, null=True, upload_to='resumes/')),
                ('resume_text', models.CharField(blank=True, default='Here goes text about yourself: ', max_length=100, null=True)),
            ],
        ),
    ]
