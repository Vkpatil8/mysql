"""
@Author: Vishal Patil
@Date: 04-02-2022 13:45:00
"""

import connections


def export():
    connection = connections.Con.connection()
    cursor = connection.cursor()

    export_query = """select * from StateCensusData into outfile 'E:/Python/Practice 
    pro/mysqlDemo/csvFileOperations/StateCensusData.csv' """

    cursor.execute(export_query)


export()