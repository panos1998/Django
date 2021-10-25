from django.db import models
import datetime
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

# Customer custom edit by me


# class Customer(models.Model):
#     Name = models.CharField(max_length=100)
#     Surname = models.CharField(max_length=100)
#     Budget = models.IntegerField()
#     date_registered = models.DateTimeField(default=timezone.now())
#     def __str__(self):
#        return '{} {}'.format(self.Name, self.Surname)
#     def budget(self):
#        return self.Budget

#     def dateregistered (self):
#         return self.date_registered

