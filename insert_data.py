import psycopg2

database_str = "TestDB"
user_str = "postgres"
password_str = "" # PUT YOUR PASSWORD HERE
host_str = "127.0.0.1"
port_str = "5432"

def insert_vendor_list(vendor_list):
    """ insert multiple vendors into the vendors table  """
    sql = "INSERT INTO vendors(vendor_name) VALUES(%s)"
    conn = None
    try:
        #establishing the connection
        conn = psycopg2.connect(database=database_str, user=user_str, password=password_str, host=host_str, port= port_str)

        #Creating a cursor object using the cursor() method
        cursor = conn.cursor()

        #Executing an MYSQL function using the execute() method
        cursor.execute("select version()")

        #Execute the insert statement
        cursor.executemany(sql, vendor_list)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    # insert multiple vendors
    insert_vendor_list([
        ('AKM Semiconductor Inc.',),
        ('Asahi Glass Co Ltd.',),
        ('Daikin Industries Ltd.',),
        ('Dynacast International Inc.',),
        ('Foster Electric Co. Ltd.',),
        ('Murata Manufacturing Co. Ltd.',)
    ])