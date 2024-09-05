from django.urls import path
from rest_framework import routers
from django.conf.urls import include




urlpatterns = [
    path('/books/<int:pk>/', include('/books/.urls'))
]