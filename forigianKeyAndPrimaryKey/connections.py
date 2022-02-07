"""
@Author: Vishal Patil
@Date: 1-02-2022 13:45:00
"""
import mysql.connector


class Con:

    @staticmethod
    def connection():
        return mysql.connector.connect(host="localhost", database="foreign_key",
                                       username="root", password="Vkpatil8@")
