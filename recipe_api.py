import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cookbook.settings')

django.setup()

import requests
from django.conf import settings

def search(name):
  name = name.replace(' ', '%20')
  response = requests.get(f"https://api.spoonacular.com/recipes/complexSearch/?apiKey={settings.SPOONACULAR_API}&query={name}",
  headers={
        'Content-Type': 'application/json',
    },
  )
  return response.json()['results']


def get_by_id(id):
  response = requests.get(f"https://api.spoonacular.com/recipes/{id}/information/?apiKey={settings.SPOONACULAR_API}",
  headers={
        'Content-Type': 'application/json',
    },
  )
  return response.json()
