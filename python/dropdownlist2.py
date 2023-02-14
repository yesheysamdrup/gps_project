import os
import psycopg2
import pandas
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="esakor",
        user='postgres',
        password='1111')
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


#app for Thram stats and bargraph
@app.route("/thram", methods=["POST","GET"])
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT adescr, count FROM vthramdistrictwise')
    thramstats = cur.fetchall()
    df = pandas.read_sql("SELECT adescr, count(cthram) FROM vthramdistrictwise", cur)
    df.plot(kind="bar", x="District", y="Total Thrams")
    plt.show()
    cur.close()
    conn.close()
    return render_template('thramstat.html', thramstat=thramstats)

@app.route("/get_gewog", methods=["POST", "GET"])
def get_gewog():
    conn = get_db_connection()
    cur = conn.cursor()
    if request.method == 'POST':
        parent_id = request.form['parent_id']
        print(parent_id)
        cur.execute(
            "SELECT bgewog,bdescr,bdzongkhag FROM block WHERE bdzongkhag = %s", [parent_id])
        gewogs = cur.fetchall()
        print(gewogs)
    return jsonify({'htmlresponse': render_template('response.html', gewog=gewogs)})


@app.route("/get_eplot", methods=["POST", "GET"])
def get_eplot():
    conn = get_db_connection()
    cur = conn.cursor()
    if request.method == 'POST':
        plot_id = request.form['plot_id']
        print(plot_id)
        cur.execute(
            "SELECT egewog,eplotid FROM plot WHERE egewog = %s", [plot_id])
        rplot = cur.fetchall()
        print(rplot)
    return jsonify({'htmlplot': render_template('plot.html', eplot=rplot)})


if __name__ == "__main__":
    app.run(debug=True)
