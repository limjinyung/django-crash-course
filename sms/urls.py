from django.urls import path
from .views import StudentCreate, StudentDelete, StudentUpdate, viewStudent

urlpatterns = [
    path('', StudentCreate.as_view(), name='create'),
    path('delete/<pk>', StudentDelete.as_view(), name='delete'),
    path('update/<int:pk>', StudentUpdate.as_view(), name='update'),
    path('view/', viewStudent)
]