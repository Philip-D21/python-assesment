import psycopg2

host = "127.0.0.1"
database = "new_db"
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
        port=port
    )

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # SQL statement to create a table named 'users'
    create_table_query = '''
       CREATE TABLE IF NOT EXISTS users (
          user_id SERIAL PRIMARY KEY,
          username VARCHAR(50) UNIQUE NOT NULL,
          email VARCHAR(100) UNIQUE  NOT NULL,
          phone_number VARCHAR(15) NOT NULL,
          created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
       )
    '''

    # SQL statement to insert values into 'users' table
    insert_table_values = '''
     INSERT INTO users (username, email, phone_number)
     VALUES ('PAUL', 'pa@gmail.com', '70131')
    '''

    # SQL statement to update user's email
    update_user_email_query = '''
    UPDATE users SET email = 'update@gmail.com'
    WHERE username = 'PAUL'
    '''

    # SQL statement to select all users
    select_users_query = '''
    SELECT * FROM users
    '''

    # SQL statement to delete a user by username
    delete_user_query = '''
    DELETE FROM users WHERE username = 'PAUL'
    '''

    # Execute a simple query to create the table
    cursor.execute(create_table_query)
    print("Table 'users' created successfully!")

    # Insert values into the table
    cursor.execute(insert_table_values)
    print("Values inserted into 'users' table successfully!")

    # Update user's email
    cursor.execute(update_user_email_query)
    print("User's email updated successfully!")

    # Select all users
    cursor.execute(select_users_query)
    users = cursor.fetchall()
    print("All Users:")
    for user in users:
        print(user)

    # Delete a user
    cursor.execute(delete_user_query)
    print("User 'PAUL' deleted successfully!")

    # Commit the changes
    connection.commit()

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL:", error)

finally:
    # Close the cursor and connection
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed.")
