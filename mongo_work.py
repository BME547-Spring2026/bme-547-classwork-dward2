from pymongo import MongoClient

uri = "mongodb+srv://bme547_class:db_demo@bme547.ba348.mongodb.net" \
      "/?appName=BME547"

client = MongoClient(uri)
client.admin.command({'ping': 1})
database = client["db_demo"]
collection = database["reviews"]

#CRUD

def create_entry():
    entry ={
        "Reviewer": "David Ward",
        "Type": "Movie",
        "Genre": "Drama",
        "Title": "Lone Star"
    }
    r = collection.insert_one(entry)
    print(r)

def retrieve_entry():
    entry = collection.find_one({"Reviewer": "David Ward"})
    print(entry)


def retrieve_entries():
    entries = collection.find({"rating": {"$eq": 0}})
    for entry in entries:
        print(entry)


def update_record():
    entry = collection.find_one({"Title": "Rick and Morty"})
    entry["Reviewer"] = entry["reviewer"]
    collection.replace_one({"_id": entry["_id"]}, entry)

def get_genres():
    genres = collection.distinct("Genre")
    print(genres)

def delete_entry():
    collection.delete_one({"Name": "The American President"})
    # collection.delete_many({})



def main():
    # create_entry()
    # retrieve_entry()
    delete_entry()
    retrieve_entries()
    # update_record()
    # get_genres()

if __name__ == "__main__":
    main()
