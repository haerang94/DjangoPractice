from django.contrib import admin
from polls.models import Question, Choice
# Register your models here.
# 정의된 테이블이 admin화면에 보여지게 한다

admin.site.register(Question)
admin.site.register(Choice)
