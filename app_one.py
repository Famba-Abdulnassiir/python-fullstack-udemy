from http.client import ImproperConnectionState
from unicodedata import name
from flask import Flask

## this gives each file a unique name thats why we use __name__
## Flask apps use app.py then import flask from Flask  
app = Flask(__name__)

# 'https://www.google.com/'
# called our Decorator with the destination with a request like / in simple terms means home page
@app.route('/') 

## Create a Method that returns Hello world but it can return anything like Json Data 
def home():
    return "Hello world"

## This app starts the app and assigns it to port 5000 if in use please use another port number.
app.run(port=5000)
