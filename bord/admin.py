from django.contrib import admin
from .models import Post, Gallery, Profile, Skill
from django.utils.safestring import mark_safe

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['image', 'user', 'created', ]
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo_show']

    def photo_show(self, obj):
        if obj.photo:
            return mark_safe("<img src='{}' width='60' />".format(obj.photo.url))
        return None
    photo_show.__name__ = 'Фото'

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name']

