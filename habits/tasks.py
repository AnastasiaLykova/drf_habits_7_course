import requests
from config import settings


def send_message(telegram_id, message):
    token = settings.TG_API_KEY
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    data = {'chat_id': telegram_id, 'text': message}
    requests.post(url, data=data)

