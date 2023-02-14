#import psycopg2
#from psycopg2.extras import RealDictCursor
#import json

#dbHost = "localhost"
#dbPort = 5432
#dbUser = "postgres"
#dbPass = "postgres"
#dbName = "esakor"
#connString = "host='%s' port='%d' user='%s' password='%s' dbname='%s'" % (dbHost, dbPort, dbUser, dbPass, dbName)
#pg = psycopg2.connect(connString)
#mycursor = pg.cursor(cursor_factory=RealDictCursor)

#def search_thram(name, cid):
 #   mycursor.execute("SELECT * FROM Thram")
  #  myresult = mycursor.fetchall()

import psycopg2
import sys as die	
#from .logs import die
import mariadb
import pandas as pn

#import matplotlib.pyplot as plt
from sqlalchemy import create_engine

import sqlalchemy as sql

#engine = create_engine("mariadb:///?User=root&;Password=yeshey010&Database=esakor&Server=localhost&Port=3306")
con = mariadb.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    password = "root",
    database = "esakor" 
  )
df = pn.read_sql("select * from Thram where cthram=3321 and cgewog=29", con)

#con = mariadb.connect(
 #   host = "localhost",
  #  port = 3306,
   # user = "root",
    #password = "yeshey010",
    #database = "esakor" 
  #)
#cur=con.cursor()
#df = cur.execute(pn.read_sql_query("select * from Thram where cthram=3321 and cgewog=29"))
#cur.execute("select * from Thram where cthram=3321 and cgewog=29")
#df=cur
print(df)
# read in your SQL query results using pandas
#dataframe = sql.engine("""
 #           select * from Thram where cthram=3321 and cgewog=29
  #          """, con = credentials)
# return your first five rows
#dataframe.head()

uri = psycopg2.connect(
    host = "localhost",
    port = 5432,
    user = "postgres",
    password = "1111",
    database = "esakor" 
  )


def insert_data(self, df: pn.DataFrame, schema: str, table: str, chunksize: int=100) -> None:
        """This function abstracts the `INSERT` queries

        Args:
            df (pn.DataFrame): dataframe to be inserted
            schema (str): the name of the schema
            table (str): the name of the table
            chunksize (int): the number of rows to insert at the time
        """
        try:
            engine = sql.create_engine(self.uri)
            with engine.connect() as uri:
                tran = uri.begin()
                df.to_sql(
                    name=table, schema=schema,
                    con=uri, if_exists="append", index=False,
                    chunksize=chunksize, method="multi"
                )
                tran.commit()
        except Exception as e:
            if 'tran' in locals():
                tran.rollback()
            die(f"{e}")

