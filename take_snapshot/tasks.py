from __future__ import absolute_import

from celery import shared_task
#import celery

import os
import digitalocean
from datetime import datetime
from .models import Backup

today = datetime.today()
do_token = os.environ['TOKEN']
manager = digitalocean.Manager(token=do_token)

@shared_task
def do_backup():
    my_droplets = manager.get_all_droplets()
    for droplet in my_droplets:
        if droplet.status == 'active' and droplet.id == 11824639:
            droplet.take_snapshot('{0:%Y%m%d}-{1}'.format(today, droplet.name), power_off=True)
            save_backup = Backup(droplet.id, droplet.name)
            save_backup.save()
