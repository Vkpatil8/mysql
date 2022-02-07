import connections


class InsertData:
    @staticmethod
    def insert_data():
        connection = connections.Con.connection()
        cursor = connection.cursor()

        insert_data_query = """insert into one_demo (name, age, percentage, contact_no, ) VALUES ('vishal', '22', '80.20', 
            '8329235763') """

        try:
            cursor.execute(insert_data_query)
            connection.commit()
            print("insert data successfully")

        except:
            connection.rollback()

        connection.close()


if __name__ == '__main__':
    InsertData.insert_data()
