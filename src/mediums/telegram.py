import json
import logging

import requests.exceptions

from . import exceptions
from .abstract import Medium

logger = logging.getLogger(__name__)


class Telegram(Medium):

    def __init__(self, recipient, message_detail):
        self.recipient = recipient
        self.message_detail = message_detail

    def send(self) -> bool:
        try:
            response = requests.post(
                **self.get_configuration(),
                json=self.get_message_details(),
            )
            response.raise_for_status()
            response.json()
            return True
        except (requests.exceptions.Timeout, requests.HTTPError, json.JSONDecodeError) as e:
            logger.warning(f'Failed to call Telegram bot API, {e}')
            raise exceptions.TemporaryFailureException(f'{e}')
        except requests.exceptions.RequestException as e:
            logger.critical(f'Failed to call Telegram bot API, {e}')
            raise exceptions.PermanentFailureException()

    def get_recipient(self) -> str:
        return self.recipient

    def get_configuration(self) -> dict:
        return {
            'url': 'https://interview-bot.zibal.ir/notify'
        }

    def get_message_details(self) -> dict:
        return {
            'token': 'U2FsdGVkX1+Ws1214udQTxtTWlCM8pblQA5DyeKEg0w=',
            'message': self.message_detail['body']
        }
