from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

# Create your models here.


class Article(models.Model):
    title = models.CharField('Sarlavha', max_length=200)
    summary = models.TextField('Qisqaca malumot')
    body = models.TextField('To\'liq malumot')
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    data = models.DateField('Sana')
    photo = models.ImageField('Rasm' ,upload_to='images/')

    def __str__(self):
        return f"{self.title} | {self.author} | {self.data}"
    
    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.pk)])