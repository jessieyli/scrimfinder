from flask import Flask, render_template, request, redirect
import mysql.connector
import os
import datetime

app = Flask(__name__)

app.secret_key = os.urandom(24)

database = mysql.connector.connect(
    host="sql3.freesqldatabase.com",
    user="sql3375238",
    passwd="SLheWDI2kn",
    database="sql3375238"
)

db = database.cursor(buffered=True)

# @app.route('/submitteam', methods = ['POST'])
# def signup():
#     name = request.form['teamname']
#     print("The registered team is" + name + "'")
#     return redirect('/')

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == "POST":
        TeamName = request.form.get("teamname")
        GameType = request.form.get("game")
        Player1 = request.form.get("player1")
        Player2 = request.form.get("player2")
        Player3 = request.form.get("player3")
        Player4 = request.form.get("player4")
        Player5 = request.form.get("player5")
        AvgRank = request.form.get("avgrank")
        Time = request.form.get("time")
        Discord = request.form.get("discord")

        db.execute("INSERT INTO liquidhax (GameType, TeamName, Player1, Player2, Player3, Player4, Player5, Rank, Time, Discord) VALUES (%(GameType)s, %(TeamName)s, %(Player1)s, %(Player2)s, %(Player3)s, %(Player4)s, %(Player5)s, %(AvgRank)s, %(Time)s, %(Discord)s)", 
        {"GameType": GameType, "TeamName": TeamName, "Player1": Player1, "Player1": Player1, "Player2": Player2, "Player3": Player3, "Player4": Player4, "Player5": Player5, "AvgRank": AvgRank, "Time": Time, "Discord": Discord})
        
        database.commit()

        return redirect("/")
    if request.method == "GET":
        db.execute("SELECT * FROM liquidhax")
        list = db.fetchall()
        return render_template("index.html", list=list)