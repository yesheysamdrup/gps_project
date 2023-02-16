import os
import psycopg2
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="esakor",
        user='postgres',
        password='yeshey010')
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT adzongkhag, adescr FROM district')
    districts = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', district=districts)

#/<eplotid>
@app.route('/plot/<eplotid>', methods=["POST","GET"])
def get_plotid(eplotid):
    conn = get_db_connection()
    cur = conn.cursor()
    if request.method == 'GET':
        #plotid = request.form['plot_id'] # "NAJ-3101" 
        print(eplotid)
        cur.execute(
            "SELECT * FROM vthram WHERE eplotid = %s", [eplotid])
        plot = cur.fetchall()
        print(plot)
        #return jsonify(plot) 
    return jsonify({'htmltplot': render_template('get_plotid.html', eplot=plot)})
        
"""@app.route('/plot', methods=["POST","GET"])
def get_plotid(eplotid):
    conn = get_db_connection()
    cur = conn.cursor()
    if request.method == 'GET':
        #plot_id = request.form['parent_id'] # "NAJ-3101" 
        print(eplotid)
        cur.execute(
            "SELECT * FROM vthram WHERE eplotid = %s", [eplotid])
        plots = cur.fetchall()
        print(plots)
#    return jsonify({'htmlplot': render_template('plot.html', plot=plots)})
    return jsonify(plots) """


"""@app.route("/plot", methods=["POST", "GET"])
def get_eplot():
    conn = get_db_connection()
    cur = conn.cursor()
    if request.method == 'POST':
        plot_id = request.form['plot_id']
        print(plot_id)
        cur.execute(
            "SELECT * FROM plot WHERE eplotid = %s", [plot_id])
        rplot = cur.fetchall()
        print(rplot)
    return jsonify({'htmltplot': render_template('plot.html', eplot=rplot)})"""
    
if __name__ == "__main__":
    app.run(debug=True)
