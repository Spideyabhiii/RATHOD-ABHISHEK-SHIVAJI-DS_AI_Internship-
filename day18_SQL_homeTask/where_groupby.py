import sqlite3
import pandas as pd
# Connect to database
conn = sqlite3.connect("internship.db")
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS interns")
# Create interns table with stipend column
cursor.execute("""
CREATE TABLE interns (
    intern_id INTEGER PRIMARY KEY AUTOINCREMENT,
    intern_name TEXT,
    track TEXT,
    stipend INTEGER
)""")
intern_data = [
    ('Rahul', 'Data Science', 6000),
    ('Sneha', 'Web Development', 4500),
    ('Aman', 'Data Science', 7000),
    ('Priya', 'Cyber Security', 5500),
    ('Kiran', 'Web Development', 5200),
    ('Anjali', 'Data Science', 4800)
]
cursor.executemany(
    "INSERT INTO interns (intern_name, track, stipend) VALUES (?, ?, ?)",
    intern_data
)
conn.commit()
#WHERE (Filter)
query_filter = """
SELECT * FROM interns
WHERE track = 'Data Science' AND stipend > 5000;
"""
df_filter = pd.read_sql_query(query_filter, conn)
print("1️ Data Science interns with stipend > 5000:\n")
print(df_filter)
# 2 GROUP BY (Average)
# -----------------------------
query_avg = """
SELECT track, AVG(stipend) AS average_stipend
FROM interns
GROUP BY track;
"""

df_avg = pd.read_sql_query(query_avg, conn)
print("\n2️ Average stipend per track:\n")
print(df_avg)

# -----------------------------
# 3️⃣ COUNT interns per track
# -----------------------------
query_count = """
SELECT track, COUNT(*) AS total_interns
FROM interns
GROUP BY track;
"""

df_count = pd.read_sql_query(query_count, conn)
print("\n3️ Number of interns per track:\n")
print(df_count)

# Close connection
conn.close()