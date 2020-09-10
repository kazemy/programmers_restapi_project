import requests

#using requests to send requests to our endpoint by using the access token 
# that are provided when we use api/token/ endpoint within postman

headers = {}
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTk5NzY2MTExLCJqdGkiOiIxNTE1MTZiZTRiOWM0ODM4YTNjYTczNTYxZjNhZjgxZSIsInVzZXJfaWQiOjF9.PWfm_y0VWAltcLA7XhWLNFp6uAkdienaeVI8LoZCwzA'

r= requests.get('http://127.0.0.1:8000/paradigm', headers=headers)
print(r.text)
print('------------')

r= requests.get('http://127.0.0.1:8000/languages', headers=headers)
print(r.text)
print('------------')

r= requests.get('http://127.0.0.1:8000/programmer', headers=headers)
print(r.text)