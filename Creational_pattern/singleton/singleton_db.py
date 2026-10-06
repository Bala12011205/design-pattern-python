class DatabaseConnection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            # Create the unique instance if it doesn't exist
            cls._instance = super().__new__(cls)
            cls._instance.connection_status = "Connected"
            cls._instance.connection_string = "Database=MyDB;user=admin;password=secret"
            cls._instance.connection_pool = []
            cls._instance.max_connections = 10
            cls._instance.current_connections = 0


        return cls._instance


# Testing the Singleton
db1 = DatabaseConnection()
db2 = DatabaseConnection()

print(db1 is db2)  # Output: True (Both variables point to the exact same memory instance)
print(db1.connection_status)  # Output: Connected
print(db1.connection_string)  # Output: Database=MyDB;user=admin;password
print(db2.connection_status)  # Output: Connected
print(db2.connection_string)  # Output: Database=MyDB;user=admin;password
print(db1.current_connections)  # Output: 0