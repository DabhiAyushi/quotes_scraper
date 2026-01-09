import sqlite3


def init_db(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS quotes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            quote TEXT NOT NULL,
            author TEXT NOT NULL,
            tags TEXT,
            author_profile TEXT,
            UNIQUE(quote, author)
        )
    """)

    conn.commit()
    return conn


def insert_quotes(conn, quotes):
    """
    Insert quotes into database.
    """
    cursor = conn.cursor()

    for q in quotes:
        try:
            cursor.execute("""
                INSERT INTO quotes (quote, author, tags, author_profile)
                VALUES (?, ?, ?, ?)
            """, (
                q["quote"],
                q["author"],
                q["tags"],
                q["author_profile"]
            ))
        except sqlite3.IntegrityError:
            pass

    conn.commit()
