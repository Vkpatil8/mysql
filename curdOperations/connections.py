import mysql.connector


class Con:

    @staticmethod
    def connection():
        return mysql.connector.connect(host="localhost", database="foreign_key",
                                       username="root", password="Vkpatil8@")
