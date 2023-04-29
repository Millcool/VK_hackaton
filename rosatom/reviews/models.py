from django.db import models

class Review(models.Model):
    text = models.TextField()
    rating = models.IntegerField()
    positive = models.BooleanField()

    def __str__(self):
        return f'Grade: {self.rating}, {self.positive}'
from django.db import models

class User(models.Model):
    criterion1 = models.IntegerField()
    criterion2 = models.IntegerField()
    criterion3 = models.IntegerField()
    criterion4 = models.IntegerField()
    criterion5 = models.IntegerField()
    criterion1_task1_grade = models.IntegerField()
    criterion1_task2_grade = models.IntegerField()

    criterion3_task1_grade = models.IntegerField()
    criterion3_task2_grade = models.IntegerField()
    criterion3_task3_grade = models.IntegerField()
    criterion3_task4_grade = models.IntegerField()

    criterion4_task1_grade = models.IntegerField()
    criterion4_task2_grade = models.IntegerField()

    criterion5_task1_grade = models.IntegerField()
    criterion5_task2_grade = models.IntegerField()
    criterion5_task3_grade = models.IntegerField()
    criterion5_task4_grade = models.IntegerField()
    criterion5_task5_grade = models.IntegerField()