"""
@Author: Vishal Patil
@Date: 02-02-2022 13:45:00
"""

import connections


def create_trigger():
    connection = connections.Con.connection()
    cursor = connection.cursor()

