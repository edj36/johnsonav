"""
Created by Eric Johnson
"""
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

def write_calendar(email):
    """
    Connect to outlook calendar, write an event
    """
    print(email)

def read_calendar():
    """
    Read outlook calendar
    """
    return ""

@app.route("/")
def hello():
    """
    Return template for index.html
    """

    return render_template("index.html")

@app.route('/', methods=['POST'])
def my_form_post():

    input_requester_email = request.form['input_requester_email']
    print(input_requester_email)
    # send some kind of alert to display here
    write_calendar(input_requester_email)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
    # $ python app.py to run
