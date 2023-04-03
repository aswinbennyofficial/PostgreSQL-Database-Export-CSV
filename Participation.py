
import json
import psycopg2
import pandas as pd


# import json file to here
with open('config.json') as f:
       data = json.load(f)


# Connect to your postgres DB
conn = psycopg2.connect(dbname=data["dbname"],user=data["user"],host=data["host"], password=data["password"],port=data["port"])

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM participation") 

# Retrieve query results
records = cur.fetchall()


FieldTuple = [('user_id', 'event_id', 'id', 'created_at', 'updated_at', 'has_attended', 'has_attended_at','attendee_id')]


df = pd.DataFrame(FieldTuple+records)
df.to_csv('./out/participation_records.csv', index=False, header=False)


conn.close()