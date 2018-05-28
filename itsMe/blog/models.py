from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=20000)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-create_date',)

    def __str__(self):
        return self.title