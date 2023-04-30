import psycopg2

# Open a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="phonebook",
    user="postgres",
    password="password")

# Delete a user and their phone numbers by email
email = input("Enter email of user to delete: ")
cursor = conn.cursor()
cursor.execute("DELETE FROM phone_numbers WHERE user_id IN (SELECT user_id FROM users WHERE email = %s)", (email,))
cursor.execute("DELETE FROM users WHERE email = %s", (email,))
conn.commit()
cursor.close()

# Delete a user and their phone numbers by phone number
phone_number = input("Enter phone number of user to delete: ")
cursor = conn.cursor()
cursor.execute("DELETE FROM phone_numbers WHERE phone_number = %s", (phone_number,))
cursor.execute("DELETE FROM users WHERE user_id IN (SELECT user_id FROM phone_numbers WHERE phone_number = %s)", (phone_number,))
conn.commit()
cursor.close()

# Close the database connection
conn.close()