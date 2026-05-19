from django.urls import path
from .views import CustomLoginView,RegisterPage,taskList, taskDetail, taskCreate, taskUpdate,DeleteView
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page=reverse_lazy('login')), name="logout"),
    path("register/", RegisterPage.as_view(), name ='register'),

    path('',taskList.as_view(), name='tasks'),
    path('task/<int:pk>/',taskDetail.as_view(), name = 'task'),
    path('create-task/',taskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/',taskUpdate.as_view(), name = 'task-update'),
    path('task-delete/<int:pk>/',DeleteView.as_view(), name = 'task-delete'),
]