import os
from datetime import datetime 
from flask import Flask, redirect, render_template

app = Flask(__name__)
app.secret_key = "randomString123"
messages = []

def add_messages(username, message):
    """Add messages to the messages list"""
    now = datetime.now().strftime("%H:%M:%S")                         # The strftime() method takes a date/time object and then converts that to a string according to a given format.
    messages.append("{} {}: {}".format(now, username, message))

def get_all_messages():
    """Get all of the messages and seperate using a br"""
    return "<br>".join(messages)

@app.route('/')
def index():
    """Main page with instructuions"""
    return render_template("index.html")

@app.route('/<username>')                   # /<username> gets treated as a variable
def user(username):
    """Display chat messages"""
    return "<h1>Welcome, {0}</h1> {1}".format(username, get_all_messages())

@app.route("/<username>/<message>")
def send_message(username, message):
    """Create a new message and redirect back to the chat page"""
    add_messages(username, message)
    return redirect("/" + username)

app.run(host = os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)             # os.getenv('IP') to get the IP address. That's an environment variable set by 
                                                                                     # Cloud9, and also one that we set for ourselves in Heroku 
