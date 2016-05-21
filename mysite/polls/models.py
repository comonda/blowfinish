from __future__ import unicode_literals

import datetime
from django.db import models
from django.utils import timezone 

# Create your models here.
class Question(models.Model):
    def __str__(self):
        class_name = "This is " + self.question_text
        return class_name

    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    def __str__(self):
        class_name = "this is " + self.choice_text
        return class_name

    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)
