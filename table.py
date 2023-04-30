import csv
import psycopg2

# Open a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="phonebook",
    user="postgres",
    password="password")

# Open the CSV file
with open('phonebook.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row
    for row in reader:
        # Insert data into the users table
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (first_name, last_name, email) VALUES (%s, %s, %s)", row[:3])
        user_id = cursor.lastrowid
        # Insert data into the phone_numbers table
        cursor.execute("INSERT INTO phone_numbers (user_id, phone_number) VALUES (%s, %s)", (user_id, row[3]))
        conn.commit()
        cursor.close()

# Close the database connection
conn.close()