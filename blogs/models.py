from django.db import models

# Create your models here.


class BlogPost(models.Model):
    """Модель поста"""
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=5000)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Возвращает строковое представление модели"""
        return self.title

