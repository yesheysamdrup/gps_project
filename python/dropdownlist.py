#app.py
import os
import psycopg2
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
 
app = Flask(__name__)
        

DB_CONFIG = {
    "database": "esakor",
    "username": "postgres",
    "password": "yeshey010",
    "host": "localhost",
    "port": "5432"
}


# Create a flask application, flask is a package to create web application
app = Flask(__name__)

# Set the database connection URI in the app configuration

username = DB_CONFIG['username']
password = DB_CONFIG['password']
host = DB_CONFIG['host']
port = DB_CONFIG['port']
database = DB_CONFIG['database']

database_uri = f"postgresql://{username}:{password}@{host}:{port}/{database}"

app.config['SQLALCHEMY_DATABASE_URI'] = database_uri


# Create object to control SQLAlchemy from the Flask app
db = SQLAlchemy(app)

# Matches attribute district 
class Readvdistrict(db.Model):
    __tablename__ = "district"
    __table_args__ = {"schema": "public"}
    adescr = db.Column(db.Integer,primary_key = True)
    adzongkhag=db.Column(db.Text)

"""@app.route('/district', methods=['GET'])
def get_district():
  districts = []
  for district in db.session.query(Readvdistrict).all():
    del district.__dict__['_sa_instance_state']
    districts = districts.append(district.__dict__)
#  return jsonify(districts)
    distlist = districts.fetchall() 
  return render_template('index.html', distlist=distlist)"""


@app.route('/district')
def index():
    cursor = db.connection.cursor()
    cur = db.connection.cursor(db.cursors.DictCursor)
    result = cur.execute("SELECT * FROM district ORDER BY adescr")
    district = cur.fetchall() 
    return render_template('index.html', district=district)
 
@app.route("/gewog",methods=["POST","GET"])
def get_gewog():
    cur = db.connection.cursor(db.cursors.DictCursor)    
    if request.method == 'POST':
        district = request.form['district']
        print(district)
        cur.execute("SELECT * FROM block WHERE bdzongkhag = %s", [district])
        block = cur.fetchall()
    return jsonify({'htmlresponse': render_template('response.html', block=block)})
if __name__ == "__main__":
    app.run(debug=True)