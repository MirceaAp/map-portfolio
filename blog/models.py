from datetime import datetime

from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(default=datetime.now())
    content = models.TextField()

    def __str__(self):
        return self.title
