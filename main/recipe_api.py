import requests
# from django.conf import settings
SPOONACULAR_API = '104d049b37b646eeb0a5989cfbb3ff64'
def search(name):
  name = name.replace(' ', '%20')
  response = requests.get(f"https://api.spoonacular.com/recipes/complexSearch/?apiKey={SPOONACULAR_API}&query={name}",
  headers={
        'Content-Type': 'application/json',
    },
  )
  return response.json()['results']


def get_by_id(id):
  response = requests.get(f"https://api.spoonacular.com/recipes/{id}/information/?apiKey={SPOONACULAR_API}",
  headers={
        'Content-Type': 'application/json',
    },
  )
  return response.json()
