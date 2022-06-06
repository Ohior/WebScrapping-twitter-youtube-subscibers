#-*- coding: utf-8 -*-
# @Author:  Aigboje Ohiorenua
# @Date:  2022-05-30 12:29:38
# 
#    /\`.   ,'/\
#   //\\0 " 0//\\       @Last Modified by:   Your name
#  //    ,^.    \\      @Last Modified time: 2022-06-06 20:29:39
#  \\           //
#   \\         //
#

from sqlite3 import connect
import sqlite3
from flask import Flask, render_template

# create app instance
app = Flask(__name__)
# create route for the home page
@app.route('/')
def home():
    # connect to database
    con = sqlite3.connect('followers.db')
    cursor = con.cursor()
    # get all records
    try:
        records = cursor.execute('SELECT * FROM follow_stats').fetchall()
    except Exception:
        records = []
    con.close()
    return render_template("stats.html", records=records)

if __name__ == '__main__':
    app.run(port=3000, debug=True)
