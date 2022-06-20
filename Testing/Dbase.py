import sqlite3
from sqlite3 import Error


def create_connection(path):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(path)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


# insert dummy data to database
def insert_dummy_data(conn):
    sql_insert_query = """ INSERT INTO Company (column1, column2)
                            VALUES (value1, value2) """
    cur = conn.cursor()
    cur.execute(sql_insert_query)
    conn.commit()
    return cur.lastrowid


if __name__ == '__main__':
    create_connection("Dbase.db")
    try:
        conn = sqlite3.connect("Dbase.db")
        insert_dummy_data(conn)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    print("Database created and dummy data inserted")
