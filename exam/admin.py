from django.contrib import admin
from .models import User,Exam, Choice, Answer, ExamTaker, Question

admin.site.register(Exam)
admin.site.register(Choice)
admin.site.register(Answer)
admin.site.register(ExamTaker)
admin.site.register(Question)
admin.site.register(User)
