from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    todo = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)
    is_do = models.BooleanField(default=False)

    def __str__(self):
        return self.todo

    class Meta:
        ordering = ['create_data']


