from crypt import methods
from flask import Flask,jsonify, render_template,request
from more_itertools import one

app =Flask(__name__)

## just for practice lets create our store but in real life it should be a database.
## Our store can be an array with one or more dictionaries in, stored pair Values.
stores = [
    {
        'name':'my wonderful store',
        'items':[
            {
                'name':'My Items',
                'price':15.88
            }
        ]
    }
]

#POST - USED to Recieve data.
#GET - USED to send data back only.

## its too important that you think of the resources 
# in terms of routes before u start formulatin them.

@app.route('/')
def home():
    return render_template('index.html')


#POST /store data:{name:}
@app.route('/store', methods=['POST'])
def create_store():
    #Before we create a new store a browser sends in a request with data, dats the request_data
    #make sure u return it as .get_json() it will convert it to a dictionary for use in python.
    request_data = request.get_json()

    ## Create our new store from this point remember it should be a dictonary since we are 
    # dealing with key:Value pair 
    new_store = {
        'name':request_data['name'],
        'items':[]
    }

    # Add or Append our new_store to  the innitial store that we created before.
    stores.append(new_store)

    ## return a jsonfied new store for JS or browser to be able to read it. 
    return jsonify(new_store)

#GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):

    #iterate over stores
    #if the store name mathes return that one
    #if none match return an error message jsonfy{}
    #Note we jsonfy a dictionary converting it to Json that can be read by the browser.

    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message':'store not found'})
    

#GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores':stores})

#POST /store/<strin:name/item{name:,price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name':request_data['name'],
                'price':request_data['price']
            }
            
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'Message':'Store not Found'})

#GET /store/<sting:name/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):

    for store in stores:
        if store['name'] == name:
            return jsonify({'items':store['items']})
    return jsonify({'message':'store not found'})

app.run(port=5000)
