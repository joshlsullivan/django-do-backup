from celery.schedules import crontab

CELERYBEAT_SCHEDULE = {
    # Executes every Monday morning at 7:30 A.M
    'do-backup-every-sunday': {
        'task': 'tasks.do_backup',
        'schedule': crontab(hour=23, minute=27, day_of_week=0)
    },
}
