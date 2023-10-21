import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = "aitooldb"

    create_demographics_table = """ CREATE TABLE IF NOT EXISTS patients (
                                        id INTEGER PRIMARY KEY,
                                        name TEXT NOT NULL,
                                        age INTEGER,
                                        city TEXT,
                                        languages  TEXT,
                                        academics TEXT,
                                        family TEXT
                                    ); """
    
    create_session_table = """CREATE TABLE IF NOT EXISTS sessions (
                                    id integer PRIMARY KEY,
                                    patient_name text NOT NULL,
                                    session_date TEXT,
                                    notes TEXT,
                                    previous JSON, 
                                    learning TEXT,
                                    availiability_time INTEGER,
                                    budget INTERGER,
                                    FOREIGN KEY (patient_id) REFERENCES patients (id)
                                );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, create_demographics_table)
        # create tasks table
        create_table(conn, create_session_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()