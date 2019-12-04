import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello there!</h1>"

app.run(host = os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)             # os.getenv('IP') to get the IP address. That's an environment variable set by 
                                                                                     # Cloud9, and also one that we set for ourselves in Heroku 
