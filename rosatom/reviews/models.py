from django.db import models

class Review(models.Model):
    text = models.TextField()
    rating = models.IntegerField()
    positive = models.BooleanField()

    def __str__(self):
        return f'Grade: {self.rating}, {self.positive}'