import sqlite3
import pandas as pd
# Connect (creates database file if not exists)
conn = sqlite3.connect("internship.db")
cursor = conn.cursor()
# Create interns table
cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    intern_id INTEGER PRIMARY KEY AUTOINCREMENT,
    intern_name TEXT,
    track TEXT
)""")
# Create mentors table
cursor.execute("""
CREATE TABLE IF NOT EXISTS mentors (
    mentor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    mentor_name TEXT,
    track TEXT
)""")
# Insert sample data into interns
cursor.execute("DELETE FROM interns")  # clear old data
cursor.execute("DELETE FROM mentors")
intern_data = [
    ('Rahul', 'Data Science'),
    ('Sneha', 'Web Development'),
    ('Aman', 'Data Science'),
    ('Priya', 'Cyber Security')
]
mentor_data = [
    ('Mr. Sharma', 'Data Science'),
    ('Ms. Kavya', 'Web Development'),
    ('Mr. Khan', 'Cyber Security')
]
cursor.executemany("INSERT INTO interns (intern_name, track) VALUES (?, ?)", intern_data)
cursor.executemany("INSERT INTO mentors (mentor_name, track) VALUES (?, ?)", mentor_data)
conn.commit()
# INNER JOIN Query
query = """
SELECT 
    interns.intern_name,
    interns.track,
    mentors.mentor_name
FROM interns
INNER JOIN mentors
ON interns.track = mentors.track;
"""
# Load result into Pandas DataFrame
df = pd.read_sql_query(query, conn)
print("JOIN Result:\n")
print(df)
# Close connection
conn.close()