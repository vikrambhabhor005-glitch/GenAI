# import requests

# # response = requests.get('https://fakestoreapi.com/products/1')

# # print(response.json())

# # import requests

# # user = {'username': 'john_doe', 'email': 'john@example.com', 'password': 'pass123'}
# # response = requests.post('https://fakestoreapi.com/users', json=user) 
# # print(response.json())

# import requests

# response = requests.get("https://wttr.in/Dahod?format=j1")
# print(response.json()['current_condition'][0]["FeelsLikeC"])

import requests

def getwhether(city):
    response = requests.get(f"https://wttr.in/{city}?format=j1")
    return (response.json()['current_condition'][0]["FeelsLikeC"])

print(getwhether("Dahod"))
print(getwhether("Surat"))
print(getwhether("Ahmedabad"))
                                                                                