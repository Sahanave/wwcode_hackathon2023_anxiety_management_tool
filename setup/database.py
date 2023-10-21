import sqlite3
from sqlite3 import Error
import pandas as pd
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

def insert_into_patients(demo_info):
    conn = sqlite3.connect('aitool.db')
    c = conn.cursor()

    # Insert a new event with a date.
    family = demo_info['family']
    name = demo_info['name']
    age = demo_info['age']
    city = demo_info['city']
    languages = demo_info['languages']
    academics = demo_info['academics']
    
    c.execute("""
            INSERT INTO patients (name, age, city, languages, academics, family) 
            VALUES (?, ?, ?, ?, ?, ?)
            ON CONFLICT(name) 
            DO UPDATE SET
                age = excluded.age, 
                city = excluded.city, 
                languages = excluded.languages, 
                academics = excluded.academics, 
                family = excluded.family;

            """,(name, age, city, languages, academics, family))


    conn.commit()

def main():
    database = "aitool.db"

    create_demographics_table = """ CREATE TABLE IF NOT EXISTS patients (
                                        id INTEGER PRIMARY KEY,
                                        name TEXT UNIQUE,
                                        age INTEGER,
                                        city TEXT,
                                        languages  TEXT,
                                        academics TEXT,
                                        family TEXT
                                    ); """
    
    create_session_table = """CREATE TABLE IF NOT EXISTS sessions (
                                    id integer PRIMARY KEY,
                                    patient_name text UNIQUE,
                                    patient_id INTEGER,
                                    session_date TEXT,
                                    notes TEXT,
                                    previous JSON, 
                                    learning TEXT,
                                    availability_time INTEGER,
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
    conn.commit()


if __name__ == '__main__':
    main()