from flask import Flask
from flask_restful import Resource, Api

## Resources represents something that out API represents, items can be a resource, student can 
# be aresource as well. SO A resource is just a thing that our API that can return and create
#they can also be mapped as datatables

app = Flask(__name__)
api = Api(app)

#class student inherits from the resource class.
class Student(Resource):
    def get(self,name):
        return{'student':name}

#on flask_restful here is where we call from the route that points to the end point of our api.
## @app.route('/student/<string:name>') this line is the same as the below line.
api.add_resource(Student, '/student/<string:name>')

## Its the default port but to be on a better side u need to explicitly assign it to 5000
app.run(port=5000)