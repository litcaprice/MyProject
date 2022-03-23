from pymongo import MongoClient
import json

UsersDB, UIcoll, NIcoll, RIcoll = None, None, None, None

def _init_(MONGODB_TOKEN):
    global LitnailsDB, UIcoll, RIcoll
    MDB_cli = MongoClient(MONGODB_TOKEN)
    LitnailsDB = MDB_cli.Litnails
    UIcoll = LitnailsDB.UsersInfo
    RIcoll = LitnailsDB.RecordInfo

def write_to_DB(coll, args):
    if coll == "UI":
        UIcoll.insert_one(args)
    elif coll == "RI":
        RIcoll.insert_one(args)
    else:
        print("Unexpected collection to write")

def read_from_DB(coll, args):
    if coll == "UI":
        return UIcoll.find_one(args)
    elif coll == "RI":
        return RIcoll.find_one(args)
    else:
        print("Unexpected collection to read")

def read_all_from_DB(coll, args):
    if coll == "UI":
        return UIcoll.find(args)
    elif coll == "RI":
        return RIcoll.find(args)
    else:
        print("Unexpected collection to read")
''' izmenit' '''
def update_to_DB(coll, args):
    if coll == "UI":
        return UIcoll.update_one(args[0], args[1])
    elif coll == "RI":
        return RIcoll.update_one(args[0], args[1])
    else:
        print("Unexpected collection to update")

def delete_from_DB(coll, args):
    if coll == "NI":
        return NIcoll.delete_one(args)
    elif coll == "RI":
        return RIcoll.delete_one(args)
    else:
        print("Unexpected collection to update")