import connections


class AlterTable:
    @staticmethod
    def alter_table():
        connection = connections.Con.connection()
        cursor = connection.cursor()
        alter_table = """alter table one_demo add address text"""

        cursor.execute(alter_table)
        print("added column in table successfully")

        connection.close()


if __name__ == '__main__':
    AlterTable.alter_table()
