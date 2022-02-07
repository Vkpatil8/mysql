"""
@Author: Vishal Patil
@Date: 02-02-2022 13:45:00
"""

import connections


def insert_data():
    connection = connections.Con.connection()
    cursor = connection.cursor()

    insert_data_in_pk_query = """insert into students (name, surname) values ('vishal', 'patil'), ('ranjit', 
    'bhosale') """

    insert_data_in_fk_query = """insert into subject (student_id, subject_name, marks) values (1,'marathi', 80), (1,
    'hindi', 70),(1, 'english',65), (1, 'math',90), (2,'marathi', 70), (2,
    'hindi', 75),(2, 'english',75), (2, 'math',70) """

    try:
        cursor.execute(insert_data_in_pk_query)
        print("data inserted successfully")
        cursor.execute(insert_data_in_fk_query)
        print("data insert successfully")
        connection.commit()
    except:
        print("Error")
        connection.rollback()
    connection.close()


insert_data()
