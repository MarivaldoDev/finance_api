from django.test import TestCase
from api.models import User, Category
from django.urls import reverse
from rest_framework import status


class UserModelTestCase(TestCase):
    def setUp(self):
        user1 = User.objects.create_user(username="user1", email="teste123@gmail.com", password="teste", first_name="Teste", last_name="User")
        user2 = User.objects.create_user(username="user2", email="teste456@gmail.com", password="teste", first_name="Teste", last_name="User2")

        Category.objects.create(user=user1, name="Category 1")
        Category.objects.create(user=user1, name="Category 2")
        Category.objects.create(user=user2, name="Category 3")
        Category.objects.create(user=user2, name="Category 4")

    def test_user_category_list_retrieves_only_user_categories(self):
        user = User.objects.get(email="teste456@gmail.com")
        self.client.force_login(user)
        response = self.client.get(reverse("user-categories"))

        assert response.status_code == 200
        categories = response.json()
        self.assertTrue(all(category["user"] == user.pk for category in categories))

    def test_user_category_list_requires_authentication(self):
        response = self.client.get(reverse("user-categories"))

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.json(), {"detail": "As credenciais de autenticação não foram fornecidas."})
        
