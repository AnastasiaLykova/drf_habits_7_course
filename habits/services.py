import json
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from habits.models import Habit


habits = Habit.objects.all()
for habit in habits:
    periods = habit.periodicity
    time = habit.time


def periods():
    if periods == 'DAILY':
        schedule, created = IntervalSchedule.objects.get_or_create(
            every=1,
            period=IntervalSchedule.DAYS,
        )
        return schedule
    elif periods == 'WEEKLY':
        schedule, created = IntervalSchedule.objects.get_or_create(
            every=7,
            period=IntervalSchedule.DAYS,
        )
        return schedule


def create_schedule():
    return PeriodicTask.objects.create(
        interval=periods(),
        name='Habit_bot',
        task='habits.tasks.send_message',
        args=json.dumps(['arg1', 'arg2']),
        kwargs=json.dumps({'arg1': 'arg2'}),
        start_time=time,
    )
