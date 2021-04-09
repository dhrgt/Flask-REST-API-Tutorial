##step 2
#import packages

from flask import Flask
from flask_restful import Api, Resource

#create new flask app

app = Flask(__name__) #common, you do this everytime you create a flask app, like an initializer
api = Api(app) #wrap our app in an API, initializes the fact that we are using a RESTful API

##step3
#create class with whatever information we want to return
class HelloWorld(Resource): #create a resource for HelloWorld
    def get(self): #GET method request, this is what will happen when a GET request is sent to a certain URL
        return {"data":"Hello World"} #this is a dictionary, return this info in response to a GET request

#register above as a Resource
api.add_resource(HelloWorld, "/helloworld") #since HellowWorld(Resource) is a resource lets add to API. So if we sent a GET request to /helloworld, it should return "Hello World"

if __name__ == "__main__":
    app.run(debug=True)
