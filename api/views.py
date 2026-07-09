from .models import Category
from .serializers import CategorySerializer
from rest_framework import generics


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer