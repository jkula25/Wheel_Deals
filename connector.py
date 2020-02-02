from pymongo import MongoClient
from pprint import pprint

class Connector:
    def __init__(self):
        self.__client = None    # private 
        self.__db = None        # private
        self.__users = None     # private

    def connectDB(self):
        # timeoutMS = 30000
        # client = MongoClient("mongodb+srv://jkula25:monkey25@wdcluster-uohgs.gcp.mongodb.net/test?retryWrites=true&w=majority", 
        #         connect=False, 
        #         socketTimeoutMS=timeoutMS, 
        #         connectTimeoutMS=timeoutMS, 
        #         serverSelectionTimeoutMS=timeoutMS)
        self.__client = MongoClient('mongodb+srv://jkula25:monkey25@wdcluster-uohgs.gcp.mongodb.net/test?retryWrites=true&w=majority')
        # print(self.__client)

        self.__db = self.__client['wheel_deals_db']
        self.__users = self.__db['users']
        # print(self.__db)
        # print(self.__users)

        # doc = self.__users.find_one()
        # print(type(doc))
        # pprint(doc)
        # print(self.__db.list_collection_names())

    def store_user(self, name, username):
        # prevent users with the same username
        if (self.__users.find_one( {"username": username} )):
            print("Sorry, that username is already taken.")
            return
        user = {"name": name,
                "username": username,
                "total_miles": 0.0
                }
        user_id = self.__users.insert_one(user).inserted_id
        return user_id

    def get_users(self):
        return self.__users

    def delete_user(self, username):
        return self.__users.find_one_and_delete({"username": username})
    
    def list_users(self):
        for user in self.__users.find():
            pprint(user)
    

if __name__ == "__main__":
    # connect to MongoDB
    mongoDB = Connector()
    mongoDB.connectDB()
    print("----------------------------------------------------------------------------------------------------")
    # create and store a new user
    # print("ADDING NEW USER...")
    # print(mongoDB.store_user("Billy Roe", "Bilby"))
    # print("---------------------------------------")
    # pprint(mongoDB.list_users())
    # print("----------------------------------------------------------------------------------------------------")
    # print("DELETING USER...")
    # pprint(mongoDB.delete_user("Bilby"))
    # print("----------------------------------------------------------------------------------------------------")
    # print users in database
    print("USERS:")
    pprint(mongoDB.list_users())
    print("----------------------------------------------------------------------------------------------------")

