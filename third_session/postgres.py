import psycopg2

host = "127.0.0.1"
database = "postgres"
user = "postgres"
password = "admin"
port = '5432'


conn = psycopg2.connect(
    dbname=database,
    user=user,
    password=password,
    host=host
)
cur = conn.cursor()



## Create a cursor object
cur = conn.cursor()


cur.execute("""
    CREATE TABLE IF NOT EXISTS todos (
        id SERIAL PRIMARY KEY,
        task TEXT NOT NULL
    )
""")

# create tasks
def add_task(task):
    cur.execute("INSERT INTO todos (task) VALUES (%s)", (task,))
    conn.commit()

# get all task 
def get_tasks():
    cur.execute("SELECT * FROM todos")
    return cur.fetchall()

# delete a task by id
def delete_task(task_id):
    cur.execute("DELETE FROM todos WHERE id = %s", (task_id,))
    conn.commit()

# Close cursor and connection
cur.close()
conn.close()