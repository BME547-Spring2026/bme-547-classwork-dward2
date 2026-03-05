from pymongo import MongoClient

uri = ("mongodb+srv://bme547_class:db_demo@bme547.ba348.mongodb.net/"
       "?appName=BME547")
# from mongodb_connect_string import uri

client = MongoClient(uri)
database = client["db_demo"]
collection = database["reviews"]


def create_entry():
    entry = {"Reviewer": "David Ward",
             "Name": "Lone Star", "Type": "Movie", "Genre": "Drama"}
    x = collection.insert_one(entry)
    print(x.inserted_id)


def retrieve_entry():
    entry = collection.find_one({"Reviewer": "David Ward2"})
    print(entry)


def retrieve_all_entries():
    entries_cursor = collection.find()
    for entry in entries_cursor:
        print(entry)
        # print("Name: ", entry["Name"])
        # print("Type: ", entry["Type"])


def update_entry():
    entry = collection.find_one({"Reviewer": "David Ward2"})
    entry["Name"] += " 2"
    x = collection.replace_one({"_id": entry["_id"]}, entry)
    print(x)


def get_categories():
    movie_genres = collection.distinct("Genre")
    for genre in movie_genres:
        print(genre)


def delete_entry():
    x = collection.delete_one({"Reviewer": "David Ward2"})
    print(x)


def main():
    create_entry()
    # retrieve_entry()
    # update_entry()
    # delete_entry()
    # retrieve_all_entries()
    # get_categories()


class Entry:

    client = None
    database = None
    collection = None

    genres = ["Drama", "Rom-Com", "Horror", "Documentary",
              "Rap", "Rock", "Pop", "Anime", "Fiction",
              "Nonfiction", "EDM", "Disco"]

    @classmethod
    def connect(cls, database, collection):
        Entry.client = MongoClient(uri)
        Entry.database = Entry.client[database]
        Entry.collection = Entry.database[collection]

    def __init__(self, reviewer, media_type, genre, title):
        self.reviewer = reviewer
        self.media_type = media_type
        self._genre = genre
        self.title = title
        self._id = None

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, genre):
        if genre in Entry.genres:
            self._genre = genre
        else:
            raise ValueError("Genre must be one of {}".format(Entry.genre))

    def save(self):
        mongodb_dict = {
            "Reviewer": self.reviewer,
            "Genre": self.genre,
            "Title": self.title,
            "Type": self.media_type
        }
        if self._id is None:
            response = Entry.collection.insert_one(mongodb_dict)
            self._id = response.inserted_id
        else:
            mongodb_dict["_id"] = self._id
            Entry.collection.update_one({"_id": self._id}, mongodb_dict)

    @classmethod
    def get_one_from_db(cls, reviewer=None, media_type=None, genre=None, title=None):
        search_dict = {}
        if reviewer is not None:
            search_dict["Reviewer"] = reviewer
        if media_type is not None:
            search_dict["Type"] = media_type
        if genre is not None:
            search_dict["Genre"] = genre
        if title is not None:
            search_dict["Title"] = title
        result = Entry.collection.find_one(search_dict)


if __name__ == '__main__':
    main()
