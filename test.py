import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "helloworld/Dhruv/25") #concatenate http URL with the helloworld resource so it will look like https://127.0.0.1:5000/helloworld
print(response.json()) #print response in a JSON format by calling .json() method
