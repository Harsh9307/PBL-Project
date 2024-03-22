import sqlite3

# Function to create database and tables
def create_database():
    # Connect to SQLite database (or create if not exists)
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()

    # Create users table
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL,
                        role TEXT NOT NULL
                    )''')

    # Create police officers table
    cursor.execute('''CREATE TABLE IF NOT EXISTS police_officers (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        badge_number TEXT UNIQUE NOT NULL
                    )''')

    # Commit changes and close connection
    conn.commit()
    conn.close()

# Function to add initial data (dummy data)
def add_initial_data():
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()

    # Insert dummy user data
    cursor.execute('''INSERT OR IGNORE INTO users (username, password, role) 
                      VALUES ('user1', 'password1', 'user')''')
    cursor.execute('''INSERT OR IGNORE INTO users (username, password, role) 
                      VALUES ('user2', 'password2', 'user')''')

    # Insert dummy police officer data
    cursor.execute('''INSERT OR IGNORE INTO police_officers (name, badge_number) 
                      VALUES ('John Doe', '12345')''')
    cursor.execute('''INSERT OR IGNORE INTO police_officers (name, badge_number) 
                      VALUES ('Jane Smith', '67890')''')

    # Commit changes and close connection
    conn.commit()
    conn.close()

# Function to fetch all users
def get_all_users():
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()

    cursor.execute('''SELECT * FROM users''')
    users = cursor.fetchall()

    conn.close()
    return users

# Function to fetch all police officers
def get_all_police_officers():
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()

    cursor.execute('''SELECT * FROM police_officers''')
    police_officers = cursor.fetchall()

    conn.close()
    return police_officers

# Create the database and tables
create_database()

# Add initial data (dummy data)
add_initial_data()

# Example usage:
# Fetch all users
print("Users:")
for user in get_all_users():
    print(user)

# Fetch all police officers
print("\nPolice Officers:")
for officer in get_all_police_officers():
    print(officer)
