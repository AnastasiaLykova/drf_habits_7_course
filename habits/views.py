from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from habits.models import Habit
from habits.paginators import HabitListPaginator
from habits.permissions import IsCreator
from habits.serializers import HabitSerializer


class RetrieveHabitAPIView(generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsCreator]


class ListPublicHabitAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = HabitListPaginator

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_public=True)


class ListHabitAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsCreator]
    pagination_class = HabitListPaginator

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(creator=self.request.user)


class CreateHabitAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
        return super().perform_create(serializer)


class UpdateHabitAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsCreator]


class DestroyHabitAPIView(generics.DestroyAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsCreator]
