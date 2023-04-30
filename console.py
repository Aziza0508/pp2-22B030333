import psycopg2

# Open a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="phonebook",
    user="postgres",
    password="password")

# Get user input
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
email = input("Enter email: ")
phone_number = input("Enter phone number: ")

# Insert data into the users table
cursor = conn.cursor()
cursor.execute("INSERT INTO users (first_name, last_name, email) VALUES (%s, %s, %s)", (first_name, last_name, email))
user_id = cursor.lastrowid
# Insert data into the phone_numbers table
cursor.execute("INSERT INTO phone_numbers (user_id, phone_number) VALUES (%s, %s)", (user_id, phone_number))
conn.commit()
cursor.close()

# Close the database connection
conn.close()