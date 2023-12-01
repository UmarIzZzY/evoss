import psycopg2

from data.config import DATABASE

connection = psycopg2.connect(
    database=DATABASE["NAME"],
    user=DATABASE["USER"],
    password=DATABASE["PASSWORD"],
    host=DATABASE["HOST"],
    port=DATABASE["PORT"]
)

cur = connection.cursor()


def select_user(user_id):
    query = f"select * from users where user_id={user_id}"
    cur.execute(query)
    return cur.fetchone()


def insert_user(data: dict):
    ism_familiya = data.get('full_name')
    yoshi = data.get('age')
    telefon_raqam = data.get('phone_number')
    user_id = data.get('user_id')

    query = (f"""INSERT INTO users (fullname, age, phone_number, user_id)
    VALUES ('{ism_familiya}', {yoshi}, {telefon_raqam}, {user_id})""")
    cur.execute(query)
    connection.commit()
    return query

