
import sqlite3
from collections import namedtuple

DB_PATH = "data/database.db"

Class = namedtuple("Class", ["id", "name", "datetime", "instructor", "available_slots"])
Booking = namedtuple("Booking", ["id", "class_id", "client_name", "client_email"])

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_connection()
    c = conn.cursor()
    
    # Create tables
    c.execute("""
        CREATE TABLE IF NOT EXISTS classes (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            datetime TEXT NOT NULL,
            instructor TEXT NOT NULL,
            available_slots INTEGER NOT NULL
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            class_id INTEGER,
            client_name TEXT NOT NULL,
            client_email TEXT NOT NULL,
            FOREIGN KEY (class_id) REFERENCES classes(id)
        )
    """)
    conn.commit()
    conn.close()

# Seed initial data if needed
from seed_classes import seed_classes
seed_classes()

def get_all_classes():
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM classes ORDER BY datetime ASC")
    result = [Class(*row) for row in c.fetchall()]
    conn.close()
    return result

def get_class_by_id(class_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM classes WHERE id = ?", (class_id,))
    row = c.fetchone()
    conn.close()
    return Class(*row) if row else None

def reduce_slot(class_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute("UPDATE classes SET available_slots = available_slots - 1 WHERE id = ? AND available_slots > 0", (class_id,))
    updated = c.rowcount
    conn.commit()
    conn.close()
    return updated > 0

def add_booking(class_id, name, email):
    conn = get_connection()
    c = conn.cursor()
    c.execute("INSERT INTO bookings (class_id, client_name, client_email) VALUES (?, ?, ?)", (class_id, name, email))
    conn.commit()
    conn.close()

def get_bookings_by_email(email):
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM bookings WHERE client_email = ?", (email,))
    result = [Booking(*row) for row in c.fetchall()]
    conn.close()
    return result
