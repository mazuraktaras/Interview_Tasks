class DatabaseConnectorMySQL:
    def connect(self):
        # connect to MySQL engine (server)
        pass

    def open_cursor(self):
        # concrete logic here
        pass

    def select(self):
        # concrete logic here
        pass

    def insert(self, data):
        # concrete logic here
        pass

    def close_cursor(self):
        # concrete logic here
        pass

    def save_data(self):
        # concrete logic here
        pass

    def disconnect(self):
        # concrete logic here
        pass

    def connector_name(self):
        return 'I am MySQL connector!'


class DatabaseConnectorSQLLite:
    def connect(self):
        # connect to SQLLite engine (file)
        pass

    def open_cursor(self):
        # concrete logic here
        pass

    def select(self):
        # concrete logic here
        pass

    def insert(self, data):
        # concrete logic here
        pass

    def close_cursor(self):
        # concrete logic here
        pass

    def save_data(self):
        # concrete logic here
        pass

    def disconnect(self):
        # concrete logic here
        pass

    def connector_name(self):
        return 'I am SQLLite connector!'


class DatabaseConnection:

    def __init__(self, implementation):
        self.implementation = implementation

    def get_data(self):
        self.implementation.connect()
        self.implementation.open_cursor()
        self.implementation.select()
        self.implementation.close_cursor()
        self.implementation.disconnect()

    def store_data(self, data):
        self.implementation.connect()
        self.implementation.open_cursor()
        self.implementation.insert(data)
        self.implementation.save_data()
        self.implementation.close_cursor()
        self.implementation.disconnect()

    def connection_info(self):
        print(self.implementation.connector_name())


if __name__ == "__main__":

    mysql_connector = DatabaseConnectorMySQL()
    connection = DatabaseConnection(DatabaseConnectorSQLLite())

    connection.get_data()
    connection.store_data('DATA')
    connection.connection_info()

    sqllite_connector = DatabaseConnectorSQLLite()
    connection = DatabaseConnection(sqllite_connector)

    connection.get_data()
    connection.store_data('DATA')
    # connection.connection_info()
    # #
