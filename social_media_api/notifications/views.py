from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Notification

# Create your views here.
class NotificationListView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        notifications = request.user.notifications.order_by("-timestamp")
        data = [
            {
                "id": n.id,
                "actor": n.actor.username,
                "verb": n.verb,
                "target": str(n.target),
                "timestamp": n.timestamp,
                "is_read": n.is_read
            }
            for n in notifications
        ]
        return Response(data)

