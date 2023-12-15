import sqlite3

def initialize_database():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS AudioBooks (
            folder TEXT NOT NULL,
            rss_url TEXT
        )
        ''')

    conn.commit()
    conn.close()



