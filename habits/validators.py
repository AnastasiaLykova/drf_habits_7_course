from rest_framework.exceptions import ValidationError
from habits.models import Habit


class TimeToCompleteValidator:
    def __init__(self, fields):
        self.fields = fields

    def __call__(self, field):
        time = dict(field).get(self.fields)
        if time and int(time) > 120:
            raise ValidationError('Время выполнения привычки не может быть больше 120 секунд.')
        else:
            return field


class PleasantHabitValidator:

    def __init__(self, field1, field2, field3):
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3

    def __call__(self, value):
        is_pleasant = dict(value).get(self.field1)
        connected_habit = dict(value).get(self.field2)
        reward = dict(value).get(self.field3)
        if connected_habit is not None and reward is not None:
            raise ValidationError('Невозможен одновременный выбор связанной привычки и указания вознаграждения.')
        if connected_habit is not None:
            connected_habit_obj = Habit.objects.filter(pk=connected_habit.pk, is_pleasant=True)
            if len(connected_habit_obj) == 0:
                raise ValidationError(
                    'В связанные привычки могут попадать только привычки с признаком приятной привычки.')
        if is_pleasant:
            if reward is not None:
                raise ValidationError('У приятной привычки не может быть вознаграждения')
            if connected_habit is not None:
                raise ValidationError('У приятной привычки не может быть связанной привычки.')
        return value
