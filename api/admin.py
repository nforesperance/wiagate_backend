from django.contrib import admin

# Register your models here.
from .models import Quiz, Question, Exam


class ExamAdmin(admin.ModelAdmin):
    fields = ('user', 'quiz', 'score', 'quiz_total',)
    readonly_fields = ('score', 'quiz_total')

    def quiz_total(self, obj):
        return obj.quiz.number_of_question


admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Exam, ExamAdmin)
