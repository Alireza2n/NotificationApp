import logging

from celery import Celery
import settings

from mediums import exceptions
from mediums.telegram import Telegram

logger = logging.getLogger(__name__)

app = Celery(
    'tasks',
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_BACKEND_URL,
)


@app.task(bind=True, name='send_via_telegram')
def send_via_telegram(self, recipient, message_detail):
    try:
        telegram_obj = Telegram(recipient, message_detail)
        return telegram_obj.send()
    except exceptions.TemporaryFailureException as e:
        self.retry()
        logger.warning(f'Temporary Failure for task #{self.id}, {e}, Will retry.')
    except exceptions.PermanentFailureException as e:
        logger.critical(f'Permanent Failure for task #{self.id}, {e}, Will NOT retry.')
        return False
