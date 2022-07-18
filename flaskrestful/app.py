from collections.abc import Mapping
from operator import truediv
from flask import Flask, request
from flask_restful import Resource, Api,reqparse
from flask_jwt import JWT, jwt_required
##Set up JWT to work wit our App


#import the authentication handler and Identity that we implemented from security module
from security import authentication,identity

app = Flask(__name__)
# add Secret key to ure app but always make sure u dont deploy it in your works
## but since this is just for learning purposes dont be suprised if u can see it
app.secret_key ='SUS2x03b'
api = Api(app)

#jwt creates its own end point #/auth that creates its own token. jwt token
jwt = JWT(app,authentication,identity) #/auth

## By default to be on the safer side it has to be in a database but for now we shall an empy List
items = []

class Item(Resource):
    @jwt_required() #its called and authenticates the user before get method can be worked on 
    def get(self,name):
        #for from items filter out the name if exists return 200 if None return 404
        #next simply means it should give u something not null or empty dictionary.
        item = next(filter(lambda x: x['name'] == name, items),None)

        #return a dictionary of Item if it exists code 200 or else return 404
        return {'item':item}, 200 if item else 404 

        #OR u can use the for loop as used below for cleaner and short code use lambda functions.

        # for item in items:
        #     if item['name'] == name:
        #         return item
        # return {'item':None} ,404 #Add error code on return line to simplify work for F.End dev


    def post(self,name):
        # Using the same lambda iterate thru the items and find out if one already exists if no 
        #proceed with creating that Item or through an error to the user.
        if next(filter(lambda x: x['name'] == name, items),None):
            return {'message':f"An item with name {name} already exists"}, 400 

    # Get play load or data from browser by user we use request and convert it to json automatically
        data = request.get_json() 
        item = {'name':name, 'price':data['price']} #Access it from here data['ure name']
        items.append(item)  #Add the item to the items data wc may be a database or list
        return item, 201 #error code should be put after the return message,
    
    def delete(self,name):
        ## Remember in delete we want to return a new List of data minus the deleted item.
        # so we can use the global data that we have.
        global items

        #from our list return a new filtered list of data where the name is not among the name
        #that was deleted.
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message':'Item Deleted'}
    
    def put(self,name):
        #Simple steps to execute this.
        # request for our data 
        #filter it to check out if the name already exists if yes update it if no then create a new
        #one NOTE: put can be used for either creating a new item or update the exisitng one.

        #This is important to avoid error it makes sure that the data provided by the overall 
        # playload is Verified before it can get stores or worked on if no then it leave 
        # the data in the initial state.. Eg if someone doesnt provide price or puts a wrong price
        # reqparse shall instead of updating this it will throw in that error and leave data in the
        # original state before this mistake was made.

        parser = reqparse.RequestParser()
        parser.add_argument('price',
            type=float,
            required = True,
            help="This field cannot be left Blank!"
        )

       ## if we are not using the passer we use this line
       #  data = request.get_json() as out playlord

       ## Here play load shall use anything from the Request parser Load.
        data = parser.parse_args()

        item = next(filter(lambda x : x['name'] != name, items))
        if item is None:
            item = {'name':name, 'price':data['price']}
            item.append(item)
        else:
            item.update(data)
            return item

    

class Item_list(Resource):
    def get(self):
        return {'item':items}, 200

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Item_list, '/items')

#for debug = True Flask helps us to generate simple readable error messages 
#without this error messages can be a mess.
app.run(port=5000, debug=True)  