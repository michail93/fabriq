from hashlib import md5
from datetime import datetime

from django.db import models


class Application(models.Model):
    ID = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    api_key = models.CharField(max_length=80)

    def create_api_key(self):
        cur_date_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        hash_key = md5(f"{self.name}#{self.ID}#{cur_date_time}".encode())
        self.api_key = hash_key.hexdigest()
        self.save()
        return hash_key.hexdigest()
