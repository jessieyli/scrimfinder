from flask import Flask, render_template
from flask import request, redirect
import os
import datetime

app = Flask(__name__)

app.secret_key = os.urandom(24)

@app.route('/submitteam', methods = ['POST'])
def signup():
    name = request.form['teamname']
    print("The registered team is" + name + "'")
    return redirect('/')

@app.route('/')
def index():
    return render_template("index.html")