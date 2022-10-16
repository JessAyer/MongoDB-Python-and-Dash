# Author: Jessica Ayer
# C340 Client Server Development 22EW1
# Project 1
# Date Last Modified: 09/27/22

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    
    def __init__(self, username, password):
        # Initializing the MongoClient.
        # Without Authentication
        #self.client = MongoClinet('mongodb://lovalhost:54490')
        # With Authentication
        self.client = MongoClient('mongodb://%s:%s@localhost:54490' % (username, password))
        self.database = self.client['AAC']
        
    #CRUD methods
    # C --Create--
    def create(self, data):
        #verify data
        if data is not None:
            self.database.animals.insert(data)  # data should be dictionary
            success = "New account added"
            return success
        else:
            raise Exception("Invalid Entry")
            
    # R --READ--            
    #Read one document
    def read(self, data):
        #verify seach critera
        if  data is not None:
            search_results = self.database.animals.find_one(data)
            for animals in search_results:
                print(animals)
            return search_results
        
        else:
            raise Exception("No match found")
        return False
    
    # Read all matching documents
    def read_all(self, data):
        cursor = self.database.animals.find(data, {'_id': False})
        return cursor
           
            
    # U --Update--
    def update(self, query, new_data):
        # Verify a matching account exists
        if query is not None:
            self.database.animals.update_many(query, new_data)
            print("Accout succesfully updated")

        else:
            raise Exception("No match found, update failed")

        
     # D --Delete--
    def delete(self, data):
        # verify matching data exists
        if data is not None:
            self.database.animals.delete_many(data)
            print("Acounts matching data deleted") 
        else:
            raise Exception("Nothing to delete")
    
        