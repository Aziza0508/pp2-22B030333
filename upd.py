import psycopg2

# Open a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="phonebook",
    user="postgres",
    password="password")

# Get user input
email = input("Enter email of user to update: ")
new_first_name = input("Enter new first name (press enter to skip): ")
new_phone_number = input("Enter new phone number (press enter to skip): ")

# Update the user's first name if provided
if new_first_name:
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET first_name = %s WHERE email = %s", (new_first_name, email))
    conn.commit()
    cursor.close()

# Update the user's phone number if provided
if new_phone_number:
    cursor = conn.cursor()
    cursor.execute("UPDATE phone_numbers SET phone_number = %s WHERE")