import psycopg2

host = "127.0.0.1"
database = "postgres"
user = "postgres"
password = "admin"
port = '5432'

connection= None

try:
    connection = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password,
        port =port
    )

    # Create a cursor object to interact with the database
    cursor = connection.cursor()


    # SQl= statement to create a table named 'users'
    create_table_query = '''
       CREATE TABLE IF NOT EXISTS users (
          user_id SERIAL PRIMARY KEY,
          username VARCHAR(50) UNIQUE NOT NULL,
          email VARCHAR(100) UNIQUE  NOT NULL,
          phone_number VARCHAR(15) NOT NULL,
          created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
       )
'''

    insert_table_values = '''
     INSERT INTO users (username, email, phone_number)
    VALUES ('PAUL', 'pa@gmail.com', 70131)
'''

    update_user_email_query = '''
 UPDATE users SET email = 'update@gmail.com'
 WHERE username = 1
'''

   
    # Execute a simple query
    cursor.execute(create_table_query)

    cursor.execute(insert_table_values)

    cursor.execute(update_user_email_query)

  # Commit the changes
    connection.commit()

    print("Table 'users' created successfully!")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL:", error)

finally:
    # Close the cursor and connection
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed.")
