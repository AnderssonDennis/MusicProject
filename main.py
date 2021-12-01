# import helper functions from our database module
from database import run, get

# Artist table
run('''
  CREATE TABLE IF NOT EXISTS artist (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    artist_name STRING NOT NULL
 )
''')

# Album table
run('''
  CREATE TABLE IF NOT EXISTS album (
    artistid INTEGER PRIMARY KEY AUTOINCREMENT,
    album_name STRING NOT NULL,
    year_release STRING,
    FOREIGN KEY(artistid) REFERENCES arist(id)
 )
''')

# Songs table
run('''
  CREATE TABLE IF NOT EXISTS songs (
    albumid INTEGER PRIMARY KEY AUTOINCREMENT,
    song_name STRING NOT NULL,
    song_duration INTEGER NOT NULL,
    FOREIGN KEY(albumid) REFERENCES album(id)
 )
''')