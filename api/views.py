from .models import Category, Account
from .serializers import CategorySerializer, AccountSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class AccountListCreateView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UserCategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [
        IsAuthenticated
    ]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)
    
    