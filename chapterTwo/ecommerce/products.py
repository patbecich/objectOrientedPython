from .database import Database

#db = database.Database()
#db = Database()
# we will query db
# access any class or function in the database module with database.<x>
# if we want to import just Database class from database module:

# from database import Database
# db = Database()
# alternative way to import database

# we can rename the imported class to avoid ambiguity
# from database import Database as DB
# db = DB()

# import multiple specific classes
# from database import Database, Query

# don't use
# from database import *
# this will clutter the namespace, and makes it difficult to
# trace where classes come from

# --PACKAGES--

# tell Python that a folder is a package by placing an empty
# "__init__" in the folder
