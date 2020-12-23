from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=timezone.now())
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created',)


class Gallery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='image')
    created = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='gallery/')


class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='День рождения')
    skill = models.ManyToManyField(Skill, related_name='profile', verbose_name='Навыки')
    photo = models.ImageField(upload_to='user/', blank=True)
    inlines = [User]
    def __str__(self):
        return 'Профиль пользователя {}'.format(self.user.username)



