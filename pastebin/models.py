from django.db import models


class Pastes(models.Model):
    title = models.CharField(max_length=6)
    content = models.TextField()