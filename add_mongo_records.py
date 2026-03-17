from pymongo import MongoClient

uri = ("mongodb+srv://bme547_class:db_demo@bme547.ba348.mongodb.net/"
       "?appName=BME547")
# from mongodb_connect_string import uri

client = MongoClient(uri)
database = client["db_demo"]
collection = database["reviews"]


def create_entry():
    entry = {"Reviewer": "David Ward",
             "Name": "A Few Good Men",
             "Type": "Movie", "Genre": "drama"}
    x = collection.insert_one(entry)
    print(x)
    entry = {"Watcher": "David Ward",
             "Name": "The American President",
             "Type": "Movie", "Genre": "RomCom"}
    x = collection.insert_one(entry)
    entry = {"Reviewer": "David Ward",
             "Name": "Sleepless in Seattle",
             "Type": "Movie", "Genre": "Rom-Com"}
    x = collection.insert_one(entry)


def add_rating_field():
    x = collection.find()
    for entry in x:
        entry["rating"] = 0
        collection.replace_one({"_id": entry["_id"]}, entry)


add_rating_field()
