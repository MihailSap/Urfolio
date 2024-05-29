from django.contrib import admin
from .models import (
    Project,
    Comment, Reply, LikedPost,
)

# ПРОЕКТ
admin.site.register(Project)

# КОММЕНТАРИИ
admin.site.register(Comment)
admin.site.register(Reply)

# ЛАЙКИ
admin.site.register(LikedPost)



