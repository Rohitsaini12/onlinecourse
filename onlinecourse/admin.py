from django.contrib import admin
from .models import Course, Lesson, Question, Choice, Submission, Instructor, Learner


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('question_text', 'course', 'grade')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ('title', 'course')


admin.site.register(Course)
admin.site.register(Submission)
admin.site.register(Instructor)
admin.site.register(Learner)
