import requests
from celery import shared_task
from config import settings
from habits.models import Habit

habits = Habit.objects.all()
for habit in habits:
    action = habit.action
    time = habit.time
    place = habit.place
    reward = habit.reward
    if habit.connected_habit:
        pleasant_action = habit.connected_habit.action
    creator_id = int(habit.creator.telegram)


@shared_task
def send_message():
    token = settings.TG_API_KEY
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    data = {'chat_id': creator_id, 'text': f'делай {action} во время{time} тут {place} награда {reward} {pleasant_action}'}
    requests.post(url, data=data)


send_message.delay()
