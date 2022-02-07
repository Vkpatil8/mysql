"""
@Author: Vishal Patil
@Date: 02-02-2022 13:45:00
"""

import mysql.connector


class Con:

    @staticmethod
    def connection():
        return mysql.connector.connect(host="localhost", database="student_info",
                                       username="root", password="Vkpatil8@")
