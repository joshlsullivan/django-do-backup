from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Backup(models.Model):
    droplet_id = models.IntegerField()
    droplet_name = models.CharField('droplet name', max_length=180)
    droplet_backup_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.droplet_name
