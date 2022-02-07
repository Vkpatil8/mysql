"""
@Author: Vishal Patil
@Date: 1-02-2022 13:45:00
"""

import connections


def read_data():
    connection = connections.Con.connection()
    cursor = connection.cursor()

    read_data_query = """select address from addresses where name_id = (select id from identity where name = 
    'vishal') """

    cursor.execute(read_data_query)
    result = cursor.fetchall()
    for data in result:
        print(data)


read_data()
