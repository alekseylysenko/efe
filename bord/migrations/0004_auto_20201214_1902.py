# Generated by Django 3.1.4 on 2020-12-14 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bord', '0003_profile_skill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='skill',
        ),
        migrations.AddField(
            model_name='profile',
            name='skill',
            field=models.ManyToManyField(related_name='profile', to='bord.Skill'),
        ),
    ]
