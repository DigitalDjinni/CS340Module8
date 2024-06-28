from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        #USER = 'aacuser'
        #PASS = 'pittsburgh1'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30625
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            try:
                self.database.animals.insert_one(data)  # data should be dictionary            
                return True
            except Exception as e:
                print(f"Error Occurred: {e}")
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Read method to implement the R in CRUD.
    def read(self, data):
        if data is not None:
            try:
                documents = list(self.collection.find(data))
                return documents
            except Exception as e:
                print(f"Error Occurred: {e}")
                return []
        else:
            raise Exception("Nothing to read, because data parameter is empty")

 # Update method to implement the U in CRUD
    def update(self, query, update_data):
        if query is not None and update_data is not None:
            try:
                result = self.collection.update_many(query, {'$set': update_data})
                return result.modified_count
            except Exception as e:
                print(f"Error Occurred: {e}")
                return 0
        else:
            raise Exception("Query and update_data parameters cannot be empty")

    # Delete method to implement the D in CRUD
    def delete(self, data):
        if data is not None:
            try:
                result = self.collection.delete_many(data)
                return result.deleted_count
            except Exception as e:
                print(f"Error Occurred: {e}")
                return 0
        else:
            raise Exception("parameter cannot be empty")