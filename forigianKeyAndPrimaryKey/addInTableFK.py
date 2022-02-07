"""
@Author: Vishal Patil
@Date: 1-02-2022 13:45:00
"""

import connections
connections = connections.Con.connection()
cursor = connections.cursor()

insert_data_in_pk_query = """insert into identity (name) values ('vishal'), ('vaibhav')"""

insert_data_in_fk_query = """insert into addresses (name_id, address) values (1, 'limb'), (2, 'limb'),(1, 
                            'manjarde'), (1, 'tasgaon'), (2, 'sangli') """

try:
    cursor.execute(insert_data_in_pk_query)
    print("data inserted successfully")
    cursor.execute(insert_data_in_fk_query)
    print("data insert successfully")
    connections.commit()
except:
    print("Error")
    connections.rollback()
connections.close()
