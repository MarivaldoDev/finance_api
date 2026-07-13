from django.urls import path
from . import views

urlpatterns = [
    path("categories/", views.CategoryList.as_view()),
    path("user-categories/", views.UserCategoryList.as_view(), name="user-categories"),
]
