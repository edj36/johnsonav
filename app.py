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
def index_page():
    """
    Return template for index.html
    """

    return render_template("index.html")

@app.route("/request")
def request_page():
    """
    Return template for request.html
    """

    return render_template("request.html")

@app.route("/admin")
def admin_page():
    """
    Return template for index.html
    """

    return render_template("admin.html")

@app.route('/request', methods=['POST'])
def request_page_post():

    input_requester_email = request.form['input_requester_email']
    print(input_requester_email)
    # send some kind of alert to display here
    write_calendar(input_requester_email)
    return render_template("request.html")

if __name__ == "__main__":
    app.run(debug=True)
    # $ python app.py to run
