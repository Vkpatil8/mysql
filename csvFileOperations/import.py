"""
@Author: Vishal Patil
@Date: 01-02-2022 13:45:00
"""

import connections


def import_data_from_csv():
    connection = connections.Con.connection()
    cursor = connection.cursor()
    create_table_query = """create table StateCensusData (state varchar(200),Population int, AreaInSqKm int, 
    DensityPerSqKm int) """
    load_file_query = """load data local infile 'E:/Python/Practice pro/mysqlDemo/csvFileOperations/01-02-2022.csv'
    into table StateCensusData FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;
    """
    try:
        cursor.execute(create_table_query)
        print("table created")

        #cursor.execute(load_file_query)
        print("load file successfully")
        connection.commit()
    except:
        connection.rollback()
        print("error")


import_data_from_csv()
