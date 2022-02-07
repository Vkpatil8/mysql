import connections


class CreateTable:
    @staticmethod
    def create_table():
        connection = connections.Con.connection()
        cursor = connection.cursor()
        create_table_query = """create table one_demo1 (id int not null auto_increment, name varchar(300) not null, 
        age int check (age >= 18), gender enum('male', 'female', 'other'), percentage float, contact_no bigint, 
        primary key(id)) """

        cursor.execute(create_table_query)
        print("create table successfully")

        connection.close()


if __name__ == '__main__':
    CreateTable.create_table()
