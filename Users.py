
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
cur.execute("SELECT * FROM users")

# Retrieve query results
records = cur.fetchall()


FieldTuple = [("email","name","profile_pic","bio","registration_no","university_name","phone_no","github_social","twitter_social","linkedin_social","id","created_at","updated_at","gender","hash","salt","isEmailVerified","github_user_id","google_sub_id","registered_with","last_login_with","last_login_at","isPasswordSet","verification_code","isAccountVerified")]


df = pd.DataFrame(FieldTuple+records)
df.to_csv('./out/users_records.csv', index=False, header=False)


conn.close()