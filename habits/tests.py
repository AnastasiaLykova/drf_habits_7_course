from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.exceptions import ErrorDetail
from rest_framework.test import APITestCase, APIClient

from habits.models import Habit
from users.models import User


class HabitsTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email='test@mail.ru',
            is_active=True
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            creator=self.user,
            place='place',
            time='12:00',
            action='action',
            periodicity='DAILY',
            reward='reward',
        )

    def tearDown(self):
        User.objects.all().delete()
        Habit.objects.all().delete()

    def test_create_habit(self):
        data = {
            'place': 'place',
            'time': '12:00',
            'action': 'action',
            'periodicity': 'DAILY',
            'reward': 'reward',
        }
        response = self.client.post(reverse('habits:create-habit'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.count(), 2)

    def test_update_habit(self):
        data = {
            'place': 'place2',
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.patch(reverse('habits:update-habit', args=[self.habit.id]), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['place'], 'place2')

    def test_delete_habit(self):
        response = self.client.delete(reverse('habits:delete-habit', args=[self.habit.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.count(), 0)

    def test_retrieve_habit(self):
        response = self.client.get(reverse('habits:view-habit', args=[self.habit.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['time'], '12:00:00')

    def test_list_public_habit(self):
        response = self.client.get(reverse('habits:list-public-habit'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 0)

    def test_list_habit(self):
        response = self.client.get(reverse('habits:list-habit'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)

    def test_list_validators(self):
        data = {
            'is_pleasant': True,
            'connected_habit': self.habit.id,
            }
        self.client.force_authenticate(user=self.user)
        response = self.client.patch(reverse('habits:update-habit', args=[self.habit.id]), data=data)
        self.assertEqual(response.data, {'non_field_errors': [ErrorDetail(string='В связанные привычки могут попадать только привычки с признаком приятной привычки.', code='invalid')]})

        data = {
            'is_pleasant': True,
            'reward': 'reward',
            }
        self.client.force_authenticate(user=self.user)
        response = self.client.patch(reverse('habits:update-habit', args=[self.habit.id]), data=data)
        self.assertEqual(response.data, {'non_field_errors': [ErrorDetail(string='У приятной привычки не может быть вознаграждения', code='invalid')]})

        data = {'time_to_complete': '1000',}
        self.client.force_authenticate(user=self.user)
        response = self.client.patch(reverse('habits:update-habit', args=[self.habit.id]), data=data)
        self.assertEqual(response.data, {'non_field_errors': [ErrorDetail(string='Время выполнения привычки не может быть больше 120 секунд.', code='invalid')]})

