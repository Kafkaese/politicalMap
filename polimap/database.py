import sqlite3
from sqlite3 import Error
import os
import csv

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def write_all_countries_to_db(csv_path):
    
    try:
 
        # Import csv and extract data
        with open(csv_path, 'r') as fin:
            dr = csv.DictReader(fin)
            country_info = [(i['country'], i['name'], i['ruling party'], i['url'], i['position']) for i in dr]
            print(country_info)
    
        # Connect to SQLite
        sqliteConnection = sqlite3.connect(f"{os.path.dirname(__file__)}/../data/databases/wiki.db")
        cursor = sqliteConnection.cursor()
    
        # Create student table 
        cursor.execute('create table country(name varchar2(10), age int);') # <----- CONTINUE HERE
    
        # Insert data into table
        cursor.executemany(
            "insert into student (name, age) VALUES (?, ?);", student_info)
    
        # Show student table
        cursor.execute('select * from student;')
    
        # View result
        result = cursor.fetchall()
        print(result)
    
        # Commit work and close connection
        sqliteConnection.commit()
        cursor.close()
    
    except sqlite3.Error as error:
        print('Error occurred - ', error)
    
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print('SQLite Connection closed')

def instert_country(conn, country):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    sql = ''' INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()

    return cur.lastrowid


if __name__ == '__main__':
    #
    #print(os.path.dirname(__file__))
    #print(f"{os.path.dirname(__file__)}/../data/databases/wiki.db")
    create_connection(f"{os.path.dirname(__file__)}/../data/databases/wiki.db")
