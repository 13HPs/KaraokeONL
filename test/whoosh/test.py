from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID, NUMERIC, BOOLEAN, DATETIME
import os
from pymongo import MongoClient
# Connection string
connection_string = "mongodb+srv://leminh:d9wcwbu0QAfyCcLv@karaoke.bjdua.mongodb.net/karaoke?retryWrites=true&w=majority&appName=karaoke"
# Replace <password> with your actual password
client = MongoClient(connection_string)

# Database and collection
db = client.karaoke  # Connect to the database
musics_collection = db.musics  # Collection with music data
accounts_collection = db.accounts #Collection with artist data

# Query to retrieve the list of lyrics
lyrics_list = []
for music in musics_collection.find():
    music_id = str(music["_id"])
    for index, lyric in enumerate(music.get("lyrics", [])):
        lyric_content = ""
        lyric_order = index
        for text in lyric:
            lyric_content += text["word"] + " "
            lyrics_list.append({
                "music_id": music_id,
                "text": lyric_content,
                "order": index
            })
        print(lyric_content, lyric_order)
query = {"_cls": "Account.ExtendedAccount.Artist"}
artists_results = accounts_collection.find(query)
artists_list = []
for artist in artists_results:
    artist_id = str(artist["_id"])
    artists_list.append({
        "artist_id": artist_id,
        "name": artist["name"]
    })
musics_list = []
for music in musics_collection.find():
    music_id = str(music["_id"])
    music_name = music["name"]
    musics_list.append({
        "music_id": music_id,
        "name": music_name
    })
# Define schema for indexing
music_schema = Schema(name=TEXT(stored=True),
                      music_id=TEXT(stored=True), )
lyric_schema = Schema(content=TEXT(stored=True),
                      music_id=TEXT(stored=True),
                      )
artist_schema = Schema(name=TEXT(stored=True),
                       artist_id=TEXT(stored=True))

# Create index directory
if not os.path.exists("indexdir"):
    os.mkdir("indexdir")

# Create index
music_collection = create_in("indexdir", music_schema)
lyric_collection = create_in("indexdir", lyric_schema)
artist_collection = create_in("indexdir", artist_schema)

from whoosh.writing import AsyncWriter

# Open the index for writing
writer = AsyncWriter(music_collection)

# Add documents
writer.add_document(id="First Document", name="Chúng ta khong thuoc ve nhau")

# Commit the changes
writer.commit()

from whoosh.qparser import QueryParser

# Open the index for searching
with ix.searcher() as searcher:
    query = QueryParser("content", ix.schema).parse("Python")
    results = searcher.search(query)

    # Print search results
    for result in results:
        print(f"Title: {result['title']}")
        print(f"Path: {result['path']}")
