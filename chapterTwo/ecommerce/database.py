
# example exercise demonstrating use of classes imported to another module


class Database:
    'Demonstration class "Database" to be imported to "Product" module'
    pass


database = None


def initialize_database():
    global database
    database = Database()
