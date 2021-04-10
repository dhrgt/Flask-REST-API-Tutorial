from flask import Flask, request #request handles data retrieval for PUT method
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

videos_put_args = reqparse.RequestParser() #make a new request parser object and automatically parse through request that we make
videos_put_args.add_argument("name", type=str, help="Name of the video")
videos_put_args.add_argument("views", type=int, help="Views of the video")
videos_put_args.add_argument("likes", type=int, help="Likes of the video")

class Video(Resource):
    def get(self, video_id): #GET method where we pass video_id
        return videos[video_id]

    def put(self, video_id): #PUT method to put information for each video_id
        print(request.form)
        return {}

api.add_resource(Video, "/video/<int:video_id>") #send information to this request


if __name__ == "__main__":
    app.run(debug=True)
