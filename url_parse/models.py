from django.db import models


class TASK(models.Model):
    TASK_ID = models.TextField(primary_key=True, unique=True)
    STATUS = models.TextField()
    FILE_PATH = models.TextField()

