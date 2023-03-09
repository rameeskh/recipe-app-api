"""
Test for Ingredient API
"""
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Ingredient

from recipe.serializers import IngredientSerializer


INGREDIENT_URL = reverse('recipe:ingredient-list')


def detail_url(tag_id):
    """Create and return a detail url"""
    return reverse('recipe:ingredient-detail', args=[tag_id])


def create_user(email='user@example.com', password='test123'):
    """Create and return a new user"""
    return get_user_model().objects.create_user(email, password)


class PublicIngredientApiTests(TestCase):
    """Test for unauthentica API requests"""

    def setUp(self):
        client = APIClient()

    def test_auth_required(self):
        """Test authentication is required for retrieving ingredients"""
        res = self.client.get(INGREDIENT_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
        