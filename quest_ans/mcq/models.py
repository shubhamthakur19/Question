import uuid
from django.db import models

# Create your models here.


class Question_set(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1)


class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1)
    text = models.TextField(max_length=250)
    image = models.ImageField(null=True, blank=True)
    correct_ans = models.TextField(max_length=250)
    explanation = models.TextField(max_length=500)
    question_set = models.ForeignKey(Question_set, on_delete=models.CASCADE)


class Options(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1)
    option = models.TextField(max_length=250)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
