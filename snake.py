'''
CREATE TABLE user (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE user_score (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES user(id) ON DELETE CASCADE,
    score INTEGER NOT NULL,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
'''

import psycopg2

# Open a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="your_database_name",
    user="your_username",
    password="your_password")

# Prompt the user to enter their username
username = input("Enter your username: ")

# Insert the username into the user table if it doesn't already exist
cursor = conn.cursor()
cursor.execute("INSERT INTO user (username) VALUES (%s) ON CONFLICT DO NOTHING", (username,))
conn.commit()
cursor.close()

# Close the database connection
conn.close()