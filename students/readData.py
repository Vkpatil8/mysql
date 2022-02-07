"""
@Author: Vishal Patil
@Date: 02-02-2022 13:45:00
"""

import connections


def read_data():
    connection = connections.Con.connection()
    cursor = connection.cursor()

    read_data_query = """select s.name, sum(su.marks) as total_subjects from students as s left join subject as su on s.id = 
    su.student_id having name = 'vishal' """

    cursor.execute(read_data_query)
    result = cursor.fetchall()
    for data in result:
        print(data)


read_data()
