from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    PERIOD = (
        ('DAILY', 'каждый день'),
        ('WEEKLY', 'раз в неделю')
    )
    creator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='создатель', **NULLABLE)
    place = models.CharField(max_length=50, verbose_name='место', **NULLABLE)
    time = models.TimeField(verbose_name='время', **NULLABLE)
    action = models.TextField(verbose_name='действие', **NULLABLE)
    is_pleasant = models.BooleanField(verbose_name='признак приятной привычки', default=False)
    connected_habit = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='связанная привычка', **NULLABLE)
    periodicity = models.CharField(max_length=15, verbose_name='периодичность', choices=PERIOD, default='DAILY')
    reward = models.TextField(verbose_name='вознаграждение', **NULLABLE)
    time_to_complete = models.PositiveIntegerField(default=120, verbose_name='длительность выполнения, с')
    is_public = models.BooleanField(verbose_name='признак публичности', default=False)

    def __str__(self):
        return f"{self.creator} {self.place} {self.time} {self.action}"

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
