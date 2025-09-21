from django.shortcuts import render

# Create your views here.
# api/views.py

from rest_framework import generics
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework import permissions

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Existing BookList view can remain or be removed if you want to use only the ViewSet.

class BookViewSet(viewsets.ModelViewSet):
    
    """
    ViewSet for managing Book objects.
    Requires authentication for all actions.
    Only admin users can delete books.
    """
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can access

    def get_permissions(self):
        # Customize permissions for delete action
        if self.action == 'destroy':
            permission_classes = [permissions.IsAdminUser]  # Only admins can delete
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]