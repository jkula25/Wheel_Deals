from pymongo import MongoClient
from pprint import pprint


def connectDB():
    # timeoutMS = 30000
    # client = MongoClient("mongodb+srv://jkula25:monkey25@wdcluster-uohgs.gcp.mongodb.net/test?retryWrites=true&w=majority", 
    #         connect=False, 
    #         socketTimeoutMS=timeoutMS, 
    #         connectTimeoutMS=timeoutMS, 
    #         serverSelectionTimeoutMS=timeoutMS)
    client = MongoClient('mongodb://jkula25:monkey25@wdcluster-uohgs.gcp.mongodb.net/wheel_deals_db?retryWrites=true&w=majority')
    print(client)

    db = client['wheel_deals_db']
    users = db['users']

    print(db)
    print(users)

    myCursor = db.users.find()

    print(type(myCursor))
    array = list()
    array.append(myCursor)
    print(array)
  

if __name__ == "__main__":
    # connect to MongoDB
    connectDB()
    # print users in database