import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = r"C:\sqlite\db\pythonsqlite.db"

    sql_create_user_credentials_table = """ CREATE TABLE IF NOT EXISTS UserCredentials (
                                        id text PRIMARY KEY,
                                        password text NOT NULL
                                    ); """

    sql_create_client_information_table = """CREATE TABLE IF NOT EXISTS ClientInformation (
                                    id text PRIMARY KEY,
                                    Full_Name varchar(50)  not null,
                                    Address1  varchar(100) not null,
                                    Address2  varchar(100) not null,
                                    City      varchar(100) not null,
                                    State     varchar(5)   not null,
                                    Zipcode   varchar(9)   not null                         
                                );"""
    sql_create_fuel_quote_table = """CREATE TABLE IF NOT EXISTS FuelQuote (
                                        id integer PRIMARY KEY,
                                        gallsRequested  integer      not null,
                                        deliveryAddress varchar(100) not null,
                                        deliveryDate    date         not null,
                                        suggPrice       integer      not null,
                                        total           decimal      not null
                                    );"""
    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create UserCredentials table
        create_table(conn, sql_create_user_credentials_table)

        # create ClientInformation table
        create_table(conn, sql_create_client_information_table)

        # create FuelQuote table
        create_table(conn, sql_create_fuel_quote_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
