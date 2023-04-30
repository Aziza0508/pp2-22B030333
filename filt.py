import psycopg2

# Open a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="phonebook",
    user="postgres",
    password="password")

# Query all users and their phone numbers
cursor = conn.cursor()
cursor.execute("SELECT u.first_name, u.last_name, p.phone_number FROM users u INNER JOIN phone_numbers p ON u.user_id = p.user_id")
results = cursor.fetchall()
for row in results:
    print(row)
cursor.close()

# Query all users with a specific phone number
phone_number = input("Enter phone number to search: ")
cursor = conn.cursor()
cursor.execute("SELECT u.first_name, u.last_name FROM users u INNER JOIN phone_numbers p ON u.user_id = p.user_id WHERE p.phone_number = %s", (phone_number,))
results = cursor.fetchall()
for row in results:
    print(row)
cursor.close()

# Close the database connection
conn.close()