"""
Test for Recipe APIs.
"""
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Recipe

from recipe.serializers import RecipeSerializer


def create_recipe(user, **params):
    """Create and return a sample Recipe"""
    defaults = {
        'title': 'Sample Recipe Title',
        'time_minutes':22,
        'price':Decimal('5.25'),
        'description': 'Sample Recipe Description',
        'links': 'http://example.com/recipe.pdf',
    }
    defaults.update(params)

    recipe = Recipe.objects.create(user=user, **defaults)
    return recipe
