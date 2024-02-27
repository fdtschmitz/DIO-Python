from flask import *
from pyngrok import ngrok
import threading
import random as r

port = "5000"
secrets = ".secrets.txt"

with open(secrets, 'r') as file:
    secret = file.read()

ngrok.set_auth_token(secret)
public_url = ngrok.connect(port).public_url
print(public_url)

app = Flask(__name__)
app.config["BASE_URL"] = public_url

d = [
    {
        "Number": "1",
        "Name": "Mahesh",
        "Age": "25",
        "City": "Bangalore",
        "Country": "India"
    },
    {
        "Number": "2",
        "Name": "Alex",
        "Age": "26",
        "City": "London",
        "Country": "UK"
    },
    {
        "Number": "3",
        "Name": "David",
        "Age": "27",
        "City": "San Francisco",
        "Country": "USA"
    },
    {
        "Number": "4",
        "Name": "John",
        "Age": "28",
        "City": "Toronto",
        "Country": "Canada"
    },
    {
        "Number": "5",
        "Name": "Chris",
        "Age": "29",
        "City": "Paris",
        "Country": "France"
    }
]

@app.route('/')
def home():
    """
    The entire line below must be written in a single line.
    """
    return "<marquee><h3> TO CHECK INPUT ADD '/input' TO THE URL AND TO CHECK OUTPUT ADD '/output' TO THE URL.</h3></marquee>"


@app.route("/input") # Code to assign Input URL in our app to function input.
def input():
    return jsonify(d) # "d" is the dictionary we defined


@app.route('/output', methods=['GET','POST']) #output page
def predjson():
    pred = r.choice(["positive", "negative"])

    for person in d:
        person["prediction"] = pred
    return jsonify(d)


threading.Thread(target=app.run, kwargs={"use_reloader": False}).start()


