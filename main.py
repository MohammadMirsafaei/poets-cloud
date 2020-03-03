import sqlite3
from sqlite3 import Error

class DB:
    def __init__(self,file):
        self.db_file = file
    
    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_file)
            print("- Connected to database...\n")
        except Error as e:
            print(e)


def main():
    database = DB("ganjoor.s3db")
    database.connect();


if __name__ == "__main__":
    main()