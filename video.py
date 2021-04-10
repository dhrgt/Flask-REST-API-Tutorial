from flask import Flask, request #request handles data retrieval for PUT method
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

videos_put_args = reqparse.RequestParser() #make a new request parser object and automatically parse through request that we make
videos_put_args.add_argument("name", type=str, help="Name of the video", required=True)
videos_put_args.add_argument("views", type=int, help="Views of the video", required=True)
videos_put_args.add_argument("likes", type=int, help="Likes of the video", required=True)

videos = {} #initializer of videos dictionary

#define function to handle scenarios where there is not data for specified video_id
def abort_if_video_id_not_exist(video_id):
    if video_id not in videos:
        abort(404, message ="Video id is not valid!") #need status code, and message = args

def abort_if_video_id_exist(video_id):
     if video_id in videos:
         abort(409, message ="Video already exists for that video_id!")

class Video(Resource):

    #return
    def get(self, video_id): #GET method where we pass video_id
        abort_if_video_id_not_exist(video_id) #run abort function if video_id does not exist
        return videos[video_id]

    #create
    def put(self, video_id): #PUT method to put information for each video_id
        abort_if_video_id_exist(video_id)
        videos[video_id] = videos_put_args.parse_args()
        return videos[video_id], 201

    #delete
    def delete(self, video_id):
        abort_if_video_id_not_exist(video_id)
        del videos[video_id] #delete the video_id in the request
        return '', 204 #204 means deleted successfully


api.add_resource(Video, "/video/<int:video_id>") #send information to this request


if __name__ == "__main__":
    app.run(debug=True)
