from flask import Flask, request, jsonify # using library from flask, jsonify is functionality json
from flask_sqlalchemy import SQLAlchemy # package created to work easier with database
# import os

DB_CONFIG = {
    "database": "esakor",
    "username": "postgres",
    "password": "yeshey010",
    "host": "localhost",
    "port": "5432"
}
# Notice, normally this is set with environment variables on the server
# machine do avoid exposing the credentials. Something like
# DB_CONFIG = {}
# DB_CONFIG['database'] = os.environ.get('DATABASE')
# DB_CONFIG['username'] = os.environ.get('USERNAME')
# ...

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


# Matches attribute vthram 
class ReadvThram(db.Model):
    __tablename__ = "vthram"
    __table_args__ = {"schema": "public"}
    adescr = db.Column(db.Text)
    bdescr=db.Column(db.Text)
    cthram = db.Column(db.Integer)
    cownid = db.Column(db.Integer)
    cownname = db.Column(db.Text)
    cdzownname = db.Column(db.Text)
    otdescr = db.Column(db.Text)
    cvillage = db.Column(db.Text)
    eplotid = db.Column(db.Integer, primary_key=True)
    eplotname= db.Column(db.Text)
    etosarea = db.Column(db.Float())
    fdescr = db.Column(db.Text)
    geoshp = db.Column(db.Text)


# Matches attribute vplot.plot table 
class ReadvPlot(db.Model):
    __tablename__ = "vplot"
    __table_args__ = {"schema": "public"}
    eplotid = db.Column(db.Integer, primary_key=True)
    ethram = db.Column(db.Integer)
    etosarea = db.Column(db.Float())
    geoshp = db.Column(db.Text)


# Matches plot table 
"""class plots(db.Model):
    __tablename__ = "plot"
    __table_args__ = {"schema": "public"}
    recid=db.Column(db.Integer)
    eplotid = db.Column(db.Integer, primary_key=True)
    egewog=db.Column(db.Integer)
    ethram = db.Column(db.Integer)
    elandtype=db.Column(db.Integer)
    eplotname=db.Column(db.String)
    edzplotname=db.Column(db.String)
    evillage=db.Column(db.String)
    edzvillage=db.Column(db.String)
    eremark=db.Column(db.String)
    etosarea=db.Column(db.Float())
    created = db.Column(db.DateTime())"""

## If the tables are not created yet, we can use the create_all() method from SQLAlchemy to
## Magically create them for us using the object created above
# db.create_all()


# GET method to get all thram from the plot_geojson view
@app.route('/thram', methods=['GET'])
def get_thram():
  thrams = []
  for thram in db.session.query(ReadvThram).all():
    del thram.__dict__['_sa_instance_state']
    thrams.append(thram.__dict__)
  return jsonify(thrams)


# Create the REST/CRUD endpoints
# GET method to get a single thrams and plot using it's dz, gewog and <thram from the vthramgeojson view
@app.route('/thram/<adescr>/<bdescr>/<cthram>', methods=['GET'])
def get_thramplot(adescr, bdescr, cthram):
    thramplot = ReadvThram.query.get(adescr, bdescr, cthram)
    del thramplot.__dict__['_sa_instance_state']
    return jsonify(thramplot.__dict__)


# Create the REST/CRUD endpoints
# GET method to get a single plot using it's plotid from the vplotgeojson view
@app.route('/plot/<eplotid>', methods=['GET'])
def get_plotid(eplotid):
    plot = ReadvPlot.query.get(eplotid)
    del plot.__dict__['_sa_instance_state']
    return jsonify(plot.__dict__)

# GET method to get all plot from the plot_geojson view
@app.route('/plot', methods=['GET'])
def get_plots():
  plots = []
  for plot in db.session.query(ReadvPlot).all():
    del plot.__dict__['_sa_instance_state']
    plots.append(plot.__dict__)
  return jsonify(plots)


# POST method to insert new plot in plots
@app.route('/plot', methods=['POST'])
def post_plot():
  body = request.get_json()
  db.session.add(plots(
      body['recid'],
      body['eplotid'],
      body['ethram'], 
      body['elandtype'],
      body['eplotname'],
      body['edzplotname'],
      body['evillage'],
      body['edzvillage'],
      body['eremark'],
      body['etosarea'],
      body['created'],
      ))
  db.session.commit()
  return "Plot created"

if __name__ == '__main__':
    
    app.run(debug=True)
