import connections


class ReadTable:

    @staticmethod
    def read_table():
        connection = connections.Con.connection()
        cursor = connection.cursor()
        select_query = """select * from one_demo where name = 'vaibhav' and percentage >= '70' """

        try:
            cursor.execute(select_query)
            result = cursor.fetchall()
            for data in result:
                name = data[1]
                age = data[2]
                percentage = data[3]
                contact_no = data[4]
                print("name = %s, age=%d, percentage=%d, contact_no=%d" % (name, age, percentage, contact_no))
        except:
            print("error")


if __name__ == '__main__':
    ReadTable.read_table()
