## PostgreSQL Table To CSV

This program helps to fetch the contents in PostgreSQL to a csv including field names.

Rename 'config.example.json' to 'config.json' and inert the necessary credentials in the json file.

change 'participation' to your required table name on the program to get the required table name.
```python
cur.execute("SELECT * FROM participation") 
```


### Requirements:

Required python packages:
- json
- psycopg2
- pandas

Install the packages by the following commands:
```bash
pip install psycopg2-binary
```

```bash
pip install pandas
```

### Excecution
- Run the python file Main.py
- Choose any one option out of the 3 choice
- Output csv will be saved in the 'output' folder


