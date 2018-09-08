from django.contrib import admin
from .models import Thread, Comment

class CommentModelAdmin(admin.ModelAdmin):
    list_display=["__str__", "timestamp"]
    class Meta:
        model=Comment

class ThreadModelAdmin(admin.ModelAdmin):
    list_display=["__str__", "timestamp"]
    class Meta:
        model=Thread

admin.site.register(Thread, ThreadModelAdmin)
admin.site.register(Comment, CommentModelAdmin)
