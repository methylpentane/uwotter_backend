import uuid
from django.db import models


# Create your models here.
class MyUser(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    name = models.CharField(
        max_length=64,
        unique=False,
        null=False,
    )
    password = models.CharField(
        max_length=64,
        null=False,
    )

    def __str__(self):
        return self.name
