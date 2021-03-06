import sqlite3
from sqlite3 import Error
from wordcloud_fa import WordCloudFa

class DB:
    def __init__(self,file):
        self.db_file = file
    
    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_file)
            print("- Connected to database...\n")
        except Error as e:
            print(e)
    
    def select(self,query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows


def main():
    database = DB("ganjoor.s3db")
    database.connect()
    rows = database.select("""select p.cat_id,v.text 
                                from poem as p join verse as v on p.id=v.poem_id 
                                where p.cat_id=24
                            """)
 
    f = open("verses.txt","w")
    for r in rows:
        f.write(r[1])
        f.write('\n')
    f.close()

    wc = WordCloudFa(width=1200, height=800)
    with open('verses.txt', 'r') as file:
        text = file.read()
    word_cloud = wc.generate(text)
    image = word_cloud.to_image()
    image.show()
    image.save('hafez.png')


if __name__ == "__main__":
    main()