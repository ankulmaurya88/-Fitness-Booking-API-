
# import sqlite3
# import os

# DB_PATH = "data/database.db"

# classes = [
#     (1, "Yoga", "2025-06-18 07:00", "Aarti", 5),
#     (2, "Zumba", "2025-06-19 09:00", "Rahul", 3),
#     (3, "HIIT", "2025-06-20 18:00", "Sneha", 4),
# ]

# def seed_classes():
#     # Ensure DB folder exists
#     os.makedirs("data", exist_ok=True)
#     conn = sqlite3.connect(DB_PATH)
#     c = conn.cursor()

#     for cls in classes:
#         c.execute("""
#             INSERT OR IGNORE INTO classes (id, name, datetime, instructor, available_slots)
#             VALUES (?, ?, ?, ?, ?)
#         """, cls)

#     conn.commit()
#     conn.close()


# seed_classes.py

import sqlite3
import os

DB_PATH = "data/database.db"

classes = [
    (1, "Yoga", "2025-06-18 07:00", "Aarti", 5),
    (2, "Zumba", "2025-06-19 09:00", "Rahul", 3),
    (3, "HIIT", "2025-06-20 18:00", "Sneha", 4),
]

def seed_classes():
    try:
        # Ensure 'data/' directory exists
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        # Ensure 'classes' table exists before inserting
        c.execute("""
            CREATE TABLE IF NOT EXISTS classes (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                datetime TEXT NOT NULL,
                instructor TEXT NOT NULL,
                available_slots INTEGER NOT NULL
            )
        """)

        for cls in classes:
            c.execute("""
                INSERT OR IGNORE INTO classes (id, name, datetime, instructor, available_slots)
                VALUES (?, ?, ?, ?, ?)
            """, cls)

        conn.commit()
        print("✅ Seed data inserted.")
    except Exception as e:
        print("❌ Error seeding classes:", e)
    finally:
        conn.close()
