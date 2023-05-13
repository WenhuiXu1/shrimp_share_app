import psycopg2
import psycopg2.extras
import os
from dotenv import load_dotenv
load_dotenv()

db_URL = os.environ.get("DATABASE_URL")

def sql(query, parameters=[]):
    connection = psycopg2.connect(db_URL) #open connection
    cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) # we use the cursor to run SQL commands
    cursor.execute(query, parameters) #beginning of transaction
    results = cursor.fetchall()
    connection.commit() # end transation, just so it is not keeping running until the next thing comes up.
    connection.close() # close connection 
    return results

# def sql(query, parameters=[]):
#     connection = psycopg2.connect(db_URL) #open connection
#     cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) # we use the cursor to run SQL commands
#     cursor.execute(query, parameters) #beginning of transaction
#     result = cursor.fetchone()
#     connection.close() # close connection 
#     return result

