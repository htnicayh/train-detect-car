from distutils.sysconfig import PREFIX
# from sqlite3 import connect
from sys import path

path.append('..')

from constant.constant import PREFIX_DATABASE, DATABASE_NAME
from constant.queries import DROP_PARK, DROP_SLOT, GENERATE_PARK, GENERATE_SLOT


from sqlite3 import connect

prefix = DATABASE_NAME + '.' + PREFIX_DATABASE
# prefix = '*.sqlite'

current_connection = connect(prefix)

def connection():
    print('Database is connecting ...')
    queries = [DROP_PARK, DROP_SLOT, GENERATE_PARK, GENERATE_SLOT]

    try:
        print('Generate database in processing ...')
        for qr in queries:
            current_connection.execute(qr)

        print('Generate success !')
        current_connection.commit()

        return current_connection
    except current_connection.Error as err:
        print('Failed in generate database rollback: {}'.format(err))

        current_connection.rollback()
    finally:
        print('Generate closing.')
        current_connection.close()

def get_connection():
    return current_connection

# Test connection
# If success: <sqlite3.Connection object at 0x7fde8e995c60>
def execute(query):
    current_connection.execute(query)
    print('Executed success')

