from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import MenuItem, BookingTable
from .serializers import MenuItemSerializer, BookingTableSerializer
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def index2(request):
    return render(request, 'index2.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class BookingTableViewSet(viewsets.ModelViewSet):
   queryset = BookingTable.objects.all()
   serializer_class = BookingTableSerializer
   permission_classes = [IsAuthenticated] 