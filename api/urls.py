from django.urls import path
from . import views

urlpatterns = [
    path("accounts/", views.AccountListCreateView.as_view()),
    path("categories/", views.CategoryList.as_view()),
    path("user-categories/", views.UserCategoryList.as_view(), name="user-categories"),
]
