from django.shortcuts import render
from owner.models import Categories,Products
from rest_framework.viewsets import ModelViewSet
from api.serializers import CategorySerializer,ProductSerializer
from rest_framework import authentication,permissions

# Create your views here.

class CategoryView(ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    # authentication_classes = [authentication.BasicAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

class ProductsView(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Products.objects.filter(category=self.request.category)
