# Определение модели Review в файле models.py приложения reviews

from django.db import models

class Review(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
    status = models.CharField(max_length=10, choices=[('positive', 'Positive'), ('negative', 'Negative')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
