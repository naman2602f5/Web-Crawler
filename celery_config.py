from celery import Celery


def make_celery(app):
    CELERY_BROKER_URL = 'redis://:local@localhost:6379/0'
    celery = Celery(
        app.import_name,
        backend=CELERY_BROKER_URL,
        broker=CELERY_BROKER_URL,
        include=['src.service.Tasks']
    )
    celery.conf.broker_connection_retry_on_startup = True
    celery.conf.update(app.config)
    celery.conf.update(app.config)

    return celery
