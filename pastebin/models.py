from django.db import models


class Paste(models.Model):
    title = models.CharField(max_length=7, db_index=True)
    content = models.TextField()
    expire = models.IntegerField(default=0)
