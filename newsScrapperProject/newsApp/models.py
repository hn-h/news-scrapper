from django.db import models

class News(models.Model):
    title=models.CharField(max_length=200)
    image=models.URLField()
    url=models.URLField()

    def __str__(self):
        return self.title
