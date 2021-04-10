import requests

BASE = "http://127.0.0.1:5000/"

data = [{"name": "How to cut an avocado", "views":40000, "likes":100000},
        {"name": "The story of risk", "views":200000, "likes": 180000},
        {"name": "The rise of Dhruv", "views":300000, "likes": 300000}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i]) #concatenate http URL with the helloworld resource so it will look like https://127.0.0.1:5000/helloworld
    print(response.json()) #print response in a JSON format by calling .json() method

input()
response = requests.delete(BASE + "video/0") #delete first video (index = 0)
print(response)

input()
response = requests.get(BASE + "video/1")
print(response.json())
