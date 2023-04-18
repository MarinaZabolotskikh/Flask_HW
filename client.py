import requests

response = requests.post('http://127.0.5000/ads/',
                         json={'heading': 'python',
                               'description': 'about python',
                               'owner': 'user_3',
                               }
                         )

response = requests.get('http://127.0.5000/ads/1')

# response = requests.delete('http://127.0.5000/ads/1')

print(response.status_code)

print(response.text)
