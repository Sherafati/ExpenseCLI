import sqlite3
from datetime import datetime

def init():
    conn = sqlite3.connect("./expenses.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS expenses (
        amount TEXT,
        title INT,
        date text,
        message text       
    );
    """
        )

    conn.commit()
    conn.close()

def add(amount,title, msg=""):
    conn = sqlite3.connect("./expenses.db")
    cursor = conn.cursor()
    currentdate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute(
        """
        INSERT INTO expenses values(?,?,?,?)
        """, (amount,title,currentdate,msg)
    )
    conn.commit()
    conn.close()

def show(cat = ""):
    conn = sqlite3.connect("./expenses.db")
    cursor = conn.cursor()
    if cat:

        cursor.execute(
            """
            SELECT * FROM expenses WHERE title= :title COLLATE NOCASE
            """, {"title" : cat}
        )
        getinfo = cursor.fetchall()
        cursor.execute(
            """
            SELECT sum(amount) FROM expenses WHERE title= :title COLLATE NOCASE
            """, {"title" : cat}
        )
        getamount = cursor.fetchone()[0]
    else:
        cursor.execute(
            """
            SELECT * FROM expenses
            """

        )
        getinfo = cursor.fetchall()
        cursor.execute(
            """
            SELECT sum(amount) FROM expenses
            """
        )

        getamount = cursor.fetchone()[0]
    return getamount, getinfo
    conn.close()

