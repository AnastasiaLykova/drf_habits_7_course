from rest_framework import serializers
from habits.models import Habit
from habits.validators import TimeToCompleteValidator, PleasantHabitValidator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [TimeToCompleteValidator(fields='time_to_complete'),
                      PleasantHabitValidator(field1='is_pleasant', field2='connected_habit', field3='reward')]
