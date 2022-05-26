from django.db import models


class Paste(models.Model):
    title = models.CharField(max_length=6, db_index=True)
    content = models.TextField()