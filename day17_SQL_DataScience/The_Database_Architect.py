import sqlite3
# 1. Create / Connect to database
conn = sqlite3.connect("internship.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    track TEXT NOT NULL,
    stipend INTEGER
)""")
intern_data = [
    (1, 'Rahul', 'Data Science', 15000),
    (2, 'Sneha', 'Web Development', 12000),
    (3, 'Arjun', 'Cyber Security', 18000),
    (4, 'Priya', 'Data Science', 16000),
    (5, 'Karan', 'Web Development', 14000)
]
cursor.executemany("INSERT OR IGNORE INTO interns VALUES (?, ?, ?, ?)", intern_data)
# 4. SELECT only name and track
cursor.execute("SELECT name, track FROM interns")
rows = cursor.fetchall()
print("Interns List (Name & Track):")
for row in rows:
    print(row)
# 5. Save and close
conn.commit()
conn.close()