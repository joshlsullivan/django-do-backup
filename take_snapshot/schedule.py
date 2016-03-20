from celery.schedules import crontab

CELERYBEAT_SCHEDULE = {
    # Executes every Monday morning at 7:30 A.M
    'do-backup-every-monday': {
        'task': 'tasks.do_backup',
        'schedule': crontab(hour=22, minute=45, day_of_week=0)
    },
}
