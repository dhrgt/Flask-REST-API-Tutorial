from flask import Flask, request #request handles data retrieval for PUT method
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy #import sqlalchemy module so that we can connect to a db instead of using memory

app = Flask(__name__)
api = Api(app) #wrap app inside Api object
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///test.db'
db = SQLAlchemy(app) #wrap app application inside sqlalchemy object

#create model
class VideoModel(db.Model): #create all of the fields inside of your model
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False) #nullable is false, meaning this field has to have some value
    views = db.Column(db.Integer, nullable = False)
    likes = db.Column(db.Integer, nullable = False)

    def __repr__(self): #method to print representation of object (could be used for internal viewing purposes)
        return f"Video(name = {name}, views = {views}, likes = {likes})" #whenever you have an f string and you put something inside curly brackets, your print the value of whatever is inside the curly bracket

#create a new instance of the VideoModel class to add data
videos_put_args = reqparse.RequestParser() #make a new request parser object and automatically parse through request that we make
videos_put_args.add_argument("name", type=str, help="Name of the video", required=True)
videos_put_args.add_argument("views", type=int, help="Views of the video", required=True)
videos_put_args.add_argument("likes", type=int, help="Likes of the video", required=True)

#update records
video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Name of the video")
video_update_args.add_argument("views", type=int, help="Views of the video")
video_update_args.add_argument("likes", type=int, help="Likes of the video")

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}

class Video(Resource):

    #retrieve
    @marshal_with(resource_fields) #serializes the return value with fields inside of the resource fields dictionary :)
    def get(self, video_id): #GET method where we pass video_id
        result = VideoModel.query.filter_by(id = video_id).first()
        if not result:
            abort(404, message= "Could not find video!")
        return result

    #create
    @marshal_with(resource_fields)
    def put(self, video_id): #PUT method to put information for each video_id
        args = videos_put_args.parse_args()
        result = VideoModel.query.filter_by(id = video_id).first()
        if result: #avoid server from crashing by adding duplicate entries
            abort(409, message= "Video_id is already taken!")
        video = VideoModel(id = video_id, name = args['name'], views = args['views'], likes = args['likes'])
        db.session.add(video) #temporarily adding video to database
        db.session.commit() #commiting video to database
        return video, 201 #return video object

    #update
    @marshal_with(resource_fields)
    def patch(self, video_id):
        args = video_update_args.parse_args()
        result = VideoModel.query.filter_by(id = video_id).first()
        if not result:
            abort(404, message= "Video does not exist, so it cannot be updated!")

        if args['name']:
            result.name = args['name'] #result. because we want to change the values of the instance
        if args['views']:
            result.views = args['views']
        if args['likes']:
            result.likes = args['likes']

        #db.session.add(result)
        db.session.commit()
        return result

    #delete
    def delete(self, video_id):
        result = VideoModel.query.filter_by(id = video_id).first()
        del result #delete the video_id in the request
        return '', 204 #204 means deleted successfully


api.add_resource(Video, "/video/<int:video_id>") #send information to this request


if __name__ == "__main__":
    app.run(debug=True)
