# import helper functions from our database module
from database import run, get

# Artist table
run('''
  CREATE TABLE IF NOT EXISTS artist (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description STRING NOT NULL,
    artist_name STRING NOT NULL
    
 )
''')

# Album table
run('''
  CREATE TABLE IF NOT EXISTS album (
    artist_id INTEGER,
    album_name STRING NOT NULL,
    description STRING NOT NULL,
    year_release STRING,
    FOREIGN KEY(artist_id) REFERENCES arist(id)
 )
''')

# Songs table
run('''
  CREATE TABLE IF NOT EXISTS songs (
    album_id INTEGER,
    song_name STRING NOT NULL,
    song_duration INTEGER NOT NULL,
    FOREIGN KEY(album_id) REFERENCES album(id)
 )
''')


artists = [
  {
    'artist_name': 'Ed Sheeran',
    'description': 'Pop',
    
  },
  {
    'artist_name': 'Elvis Presley',
    'description': 'king of rock',
  
  },
  {
    'artist_name': 'Michael Jackson',
    'description': 'king of pop',
    
  },
]