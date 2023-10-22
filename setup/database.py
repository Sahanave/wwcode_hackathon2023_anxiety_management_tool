import sqlite3
from sqlite3 import Error
import pandas as pd
from datetime import date

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

def get_patients_previous_sessions(name):

    conn = sqlite3.connect('aitool.db')
    sql = f"""SELECT 
        patients.id AS patient_id,
        patients.name AS patient_name,
        patients.age,
        patients.city,
        patients.languages,
        patients.academics,
        patients.family,
        sessions.id AS session_id,
        sessions.session_date,
        sessions.notes,
        sessions.learning,
        sessions.availability_time,
        sessions.budget
    FROM 
        patients
    INNER JOIN 
        sessions ON patients.id = sessions.patient_id
    WHERE 
        patients.name = '{name}'
    ORDER BY
        sessions.session_date; 
    """
    dataframe = pd.read_sql(sql,conn)
    return dataframe

def insert_into_session(session_info):
    from backend.therapist_dashboard import get_user_entry
    conn = sqlite3.connect('aitool.db')
    c = conn.cursor()

    # Insert a new event with a date
    patient_name = session_info['patient_name']
    user_demo_data = get_user_entry(patient_name)
    patient_id = user_demo_data['patient_id']
    today = date.today()
    session_date = str(today)
    notes = session_info['insight']
    learning = session_info['learning']
    availability_time = session_info['availability_time']
    weekly_budget = session_info['weekly_budget']
    session_activity = session_info['activities']
    
    c.execute("""
            INSERT INTO sessions (patient_name, patient_id, session_date, notes, learning, availability_time,  budget,activities) 
            VALUES (?, ?, ?, ?, ?, ?) """,(patient_name, patient_id, session_date, notes, learning, availability_time,weekly_budget,session_activity))


    conn.commit()

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
                                    learning TEXT,
                                    availability_time INTEGER,
                                    budget INTERGER,
                                    activities JSON,
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