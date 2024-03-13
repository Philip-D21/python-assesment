import psycopg2


host = "127.0.0.1"
database = "baby_db"
user = "postgres"
password = "admin"
port = '5432'



# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname=database,
    user=user,
    password=password,
    host=host,
    port=port
)



cur = conn.cursor()

# Create table if not exists
cur.execute("""
    CREATE TABLE IF NOT EXISTS baby_names (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL
    )
""")

# Extracted baby names
extracted_baby_names = ["Emma", "Liam", "Olivia", "Noah"]  



# Insert baby names into the PostgreSQL table
for name in extracted_baby_names:
    cur.execute("INSERT INTO baby_names (name) VALUES (%s)", (name,))
    
# Commit changes
conn.commit()

print("Baby names inserted into database successfully.")

# Close cursor and connection
cur.close()
conn.close()