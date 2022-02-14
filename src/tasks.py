import logging

from celery import Celery
from pottery import Redlock

import cache
import settings
from mediums import exceptions
from mediums.telegram import Telegram

logger = logging.getLogger(__name__)
redis_client = cache.redis_connect()
app = Celery(
    'tasks',
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_BACKEND_URL,
)


@app.task(bind=True, name='send_via_telegram')
def send_via_telegram(self, recipient, message_detail):
    # Create a lock for this task based hash of recipient and message_detail
    # The lock should expire in 1 minutes.
    current_task_lock = Redlock(
        key='send_via_telegram_{}_{}'.format(hash(recipient), hash(str(message_detail))),
        masters={redis_client},
        auto_release_time=60 * 1000
    )
    # Try to acquire the lock for 1 seconds, then let go.
    if current_task_lock.acquire(timeout=1):
        try:
            telegram_obj = Telegram(recipient, message_detail)
            return telegram_obj.send()
        except exceptions.TemporaryFailureException as e:
            logger.warning(f'Temporary Failure for task #{self.id}, {e}, Will retry.')
            current_task_lock.release()
            raise self.retry(exc=e)
        except exceptions.PermanentFailureException as e:
            logger.critical(f'Permanent Failure for task #{self.id}, {e}, Will NOT retry.')
            return False
