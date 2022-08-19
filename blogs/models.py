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


class Entry(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.post} - {self.name}"

    class Meta:
        verbose_name_plural = "Непонятная хрень"

