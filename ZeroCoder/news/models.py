from django.db import models
from django.contrib.auth.models import User

class News_post(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=500)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # обязательно

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

