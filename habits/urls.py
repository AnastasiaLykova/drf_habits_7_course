from django.urls import path

from habits.apps import HabitsConfig
from habits.views import RetrieveHabitAPIView, ListPublicHabitAPIView, ListHabitAPIView, CreateHabitAPIView, \
    UpdateHabitAPIView, DestroyHabitAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path('<int:pk>/', RetrieveHabitAPIView.as_view(), name='view-habit'),
    path('public/', ListPublicHabitAPIView.as_view(), name='list-public-habit'),
    path('list/', ListHabitAPIView.as_view(), name='list-habit'),
    path('create/', CreateHabitAPIView.as_view(), name='create-habit'),
    path('update/<int:pk>/', UpdateHabitAPIView.as_view(), name='update-habit'),
    path('delete/<int:pk>/', DestroyHabitAPIView.as_view(), name='delete-habit'),
]
