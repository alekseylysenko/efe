# Generated by Django 3.1.4 on 2020-12-14 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bord', '0004_auto_20201214_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='День рождения'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='skill',
            field=models.ManyToManyField(related_name='profile', to='bord.Skill', verbose_name='Навыки'),
        ),
    ]