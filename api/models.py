from uuid import uuid4

from django.db import models


class Application(models.Model):
    ID = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    api_key = models.CharField(max_length=80)

    def create_api_key(self):
        uuid_hex = uuid4().hex
        self.api_key = uuid_hex
        self.save()
        return uuid_hex
