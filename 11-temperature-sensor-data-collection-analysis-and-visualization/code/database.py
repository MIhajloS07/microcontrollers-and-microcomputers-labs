import sqlite3
from datetime import datetime
conn = sqlite3.connect("data.db")

# Define a cursor to interact with the database
c = conn.cursor()

# Create a table to store the DHT sensor data if it doesn't already exist
c.execute("""
CREATE TABLE IF NOT EXISTS dht_data(
    time TEXT,
    t1 REAL,
    h1 REAL,
    t2 REAL,
    h2 REAL
)
""")

# Function to save data to the database
def save(t1, h1, t2, h2):
    c.execute("INSERT INTO dht_data VALUES (?, ?, ?, ?, ?)",
        (datetime.now(), t1, h1, t2, h2))
    conn.commit()
