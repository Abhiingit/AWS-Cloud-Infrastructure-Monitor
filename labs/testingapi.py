'''import requests
url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

print(response.status_code)'''

'''import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

print(response.status_code)

data = response.json()
print(type(data))
print(data)
for user in data:
    print("ID:", user["id"])
    print("Name:", user["name"])
    print("Email:", user["email"])
    print("City:", user["address"]["city"])
    print("-" * 30)'''
    
    
import requests

url = "https://b4qmt5qt55.execute-api.ap-south-1.amazonaws.com/default/cloud-practical-lambda"

response = requests.get(url)

print("Status:", response.status_code)
print("Response:", response.json())