from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Notification

class NotificationListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notifications = Notification.objects.filter(recipient=request.user, read=False)
        notification_data = [{'actor': n.actor.username, 'verb': n.verb, 'timestamp': n.timestamp} for n in notifications]
        return Response({'notifications': notification_data})

