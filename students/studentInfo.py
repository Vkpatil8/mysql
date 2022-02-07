"""
@Author: Vishal Patil
@Date: 02-02-2022 13:45:00
"""

import connections


def create_table():
    connection = connections.Con.connection()
    cursor = connection.cursor()
    create_table_student_query = """create table students (id int primary key auto_increment, name varchar(
        300) not null, surname varchar(200) )"""

    create_table_student_subject_query = """create table subject (subject_id int primary key auto_increment,
    student_id int, subject_name varchar( 300) not null, marks int, foreign key (student_id) references students(id) 
    ) """

    create_table_student_marks_subject_wise_query = """create table student_marks (id int primary key auto_increment, 
    name_id int, foreign key (name_id) references identity(subject_id), address text) """

    cursor.execute(create_table_student_query)
    print("create table 1st successfully")
    cursor.execute(create_table_student_subject_query)
    print("create table 2nd successfully")
    connection.close()


create_table()
