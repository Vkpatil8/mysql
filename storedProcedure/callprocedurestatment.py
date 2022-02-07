import connections

connection = connections.Con.connection()
cursor = connection.cursor()

cursor.callproc("get_all_data_in_table")
for data in cursor.stored_results():
    print(data.fetchall())

