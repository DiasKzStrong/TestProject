import requests
from django.middleware.csrf import get_token

csrf_token = get_token(requests.request)
headers = {'X-CSRFToken': csrf_token}

print(headers)