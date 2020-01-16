from django.db import models

# Create your models here.
# 테이블을 정의함

# 장고에서 테이블은 하나의 클래스로 정의한다
# 테이블 컬럼은 클래스의 변수(속성)이다
# 테이블 클래스는 django.db.models.Model을 상속받아 정의한다


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
