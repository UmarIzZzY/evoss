import psycopg2

from data.config import DATABASE

connection = psycopg2.connect(
    database=DATABASE["database"],
    user=DATABASE["user"],
    password=DATABASE["password"],
    host=DATABASE["host"],
    port=DATABASE["port"]
)

cur = connection.cursor()


