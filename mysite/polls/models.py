from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Question(models.Model):
    def __str__(self):
        class_name = "This is " + self.question_text
        return class_name
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    def __str__(self):
        class_name = "this is " + self.choice_text
        return class_name
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)
