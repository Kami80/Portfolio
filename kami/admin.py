from django.contrib import admin
from .models import MyPage, MyCourses, Interest, Info, Skill, Resume, More, Tag, Blog

# Register your models here.
admin.site.register(MyPage)
admin.site.register(MyCourses)
admin.site.register(Interest)
admin.site.register(Info)
admin.site.register(Skill)
admin.site.register(Resume)
admin.site.register(More)
admin.site.register(Tag)
admin.site.register(Blog)