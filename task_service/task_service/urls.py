from django.contrib import admin
from django.urls import path
from task_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task/', views.task)
]
