"""
@Author: Vishal Patil
@Date: 1-02-2022 13:45:00
"""

import connections


class CreateTable:
    @staticmethod
    def create_table():
        connection = connections.Con.connection()
        cursor = connection.cursor()
        create_table_identity_query = """create table identity (id int auto_increment, name varchar(
        300) not null, primary key(id) )"""
        create_table_addresses_query = """create table addresses (id int primary key auto_increment, name_id int,
        foreign key (name_id) references identity(id), address text) """

        cursor.execute(create_table_identity_query)
        print("create table 1st successfully")
        cursor.execute(create_table_addresses_query)
        print("create table 2nd successfully")
        connection.close()


if __name__ == '__main__':
    CreateTable.create_table()
