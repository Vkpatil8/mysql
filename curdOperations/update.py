import mysql.connector


class UpdateData:
    @staticmethod
    def update_data():
        connection = mysql.connector.connect(host="localhost", database="mysql_demo",
                                             username="root", password="Vkpatil8@")
        cursor = connection.cursor()
        update_data = """update one_demo set name = 'vaibhav' where name = 'vishal' """

        try:
            cursor.execute(update_data)
            print("update successfully")
            connection.commit()
        except:
            print("unsuccessful")
            connection.rollback()

        connection.close()


if __name__ == '__main__':
    UpdateData.update_data()
