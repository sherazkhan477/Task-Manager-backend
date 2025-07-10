from django.urls import path
from . import views
from .views import TaskListCreate, TaskRetrieveUpdateDelete

urlpatterns = [
    # Home page route
    path('', views.home, name='home'),

    # Task API routes
    path('TMSys/', TaskListCreate.as_view(), name="Create-TMSys-List"),  # Ensure there is a trailing slash
    path('task/<int:pk>/', TaskRetrieveUpdateDelete.as_view(), name='task-Details'),  # Ensure there is a trailing slash
]
