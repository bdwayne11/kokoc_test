from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Test, Question, Choice, User, Color


class ChoiceAdminInline(admin.StackedInline):
    model = Choice
    min_num = 1
    extra = 0


class QuestionAdminInline(admin.StackedInline):
    model = Question
    min_num = 1
    extra = 0


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    search_fields = ('title', 'slug')
    inlines = (QuestionAdminInline,)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('text',)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ('text',)
    inlines = (ChoiceAdminInline,)


admin.site.register(User)
admin.site.unregister(Group)
admin.site.register(Color)
