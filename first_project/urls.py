from django.urls import path
from first_project import views

urlpatterns = [
    path('greeting/', views.greeting),
    path('hello/', views.hello)

]