from django.db import models
from authentication.models import CustomUser
from datetime import datetime   

# Create your models here.


class Quiz(models.Model):
    tag = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    number_of_question = models.PositiveIntegerField(default=0)
    time_minutes = models.PositiveIntegerField(default=0)
    online = models.BooleanField(default=False)
    use_date = models.BooleanField(default=False)
    start_date = models.DateTimeField(default= datetime.now, blank=True)
    end_date = models.DateTimeField(default= datetime.now, blank=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    choices = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    )
    number = models.AutoField(primary_key=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    A = models.CharField(max_length=200)
    B = models.CharField(max_length=200)
    C = models.CharField(max_length=200)
    D = models.CharField(max_length=200)
    correct = models.CharField(max_length=200, choices=choices)

    def __str__(self):
        return str(self.number)+":" + self.question
class Exam(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.quiz.name+ "("+ self.user.username+")"