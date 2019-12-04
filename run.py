import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    """ Main page with instructuions"""
    return "To send a message use /USERNAME/MESSAGE"

@app.route('/<username>')                   # /<username> gets treated as a variable
def user(username):
    return "Hi " + username

@app.route("/<username>/<message>")
def send_message(username, message):
    return "{0}: {1}".format(username, message)

app.run(host = os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)             # os.getenv('IP') to get the IP address. That's an environment variable set by 
                                                                                     # Cloud9, and also one that we set for ourselves in Heroku 
