from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('creator', 'place', 'time', 'action', 'is_pleasant', 'connected_habit',
                    'periodicity', 'reward', 'time_to_complete', 'is_public',)
    list_filter = ('creator',)
    search_fields = ('creator',)
