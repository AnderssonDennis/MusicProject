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
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    artist_id INTEGER NOT NULL,
    album_name STRING NOT NULL,
    description STRING NOT NULL,
    year_released STRING,
    FOREIGN KEY(artist_id) REFERENCES arist(id)
 )
''')

# Songs table
run('''
  CREATE TABLE IF NOT EXISTS song (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
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
    'description': 'King of rock',
  
  },
  {
    'artist_name': 'Michael Jackson',
    'description': 'King of pop',
    
  },
]


for mock_artist in artists:
  run('INSERT INTO artist VALUES(NULL, :description, :artist_name)', mock_artist)




albums = [
  {
    'album_name': 'X',
    'description': 'Ed Sheerans album',
    'year_released': '2014',
    'artist_id': '1'
    
  },
  {
    'album_name': 'Elvis christmas album',
    'description': 'Elvis most sold album',
    'year_released': '1957',
    'artist_id': '2'
  
  },
  {
    'album_name': 'Bad',
    'description': 'Michaels badest album',
    'year_released': '1987',
    'artist_id': '3'
  },
]

for mock_album in albums:
 run('INSERT INTO album VALUES(NULL, :artist_id, :album_name, :description, :year_released)', mock_album)




songs_ed = [
  {
    'song_name': 'One',
    'song_duration': '4:13',
    'artist_id': 1
  },
  {
    'song_name': 'Im a Mess',
    'song_duration': '4:06',
    'artist_id': 1
  },
  {
    'song_name': 'Sing',
    'song_duration': '3:55',
    'artist_id': 1
  },
  {
    'song_name': 'Dont',
    'song_duration': '3:39',
    'artist_id': 1
  },
  {
    'song_name': 'Nina',
    'song_duration': '3:43',
    'artist_id': 1
  },
  {
    'song_name': 'Photograph',
    'song_duration': '4:17',
    'artist_id': 1
  },  {
    'song_name': 'Bloodstream',
    'song_duration': '4:59',
    'artist_id': 1
  },
  {
    'song_name': 'Tenerife Sea',
    'song_duration': '4:00',
    'artist_id': 1
  },
  {
    'song_name': 'Runaway',
    'song_duration': '3:26',
    'artist_id': 1
  },   
  {
    'song_name': 'The Man',
    'song_duration': '4:09',
    'artist_id': 1
  },
]
# Eds albumlista
for mock_ed in songs_ed:
  run('INSERT INTO song VALUES(NULL, :artist_id, :song_name, :song_duration)', mock_ed)



songs_elvis = [
  {
    'song_name': 'Santa Claus Is Back In Town',
    'song_duration': '2:26',
    'artist_id': '2'
  },
  {
    'song_name': 'White Christmas',
    'song_duration': '2:25',
    'artist_id': '2'
  },
  {
    'song_name': 'Here Comes Santa Claus',
    'song_duration': '1:56',
    'artist_id': '2'
  },
  {
    'song_name': 'Ill Be Home for Christmas',
    'song_duration': '1:55',
    'artist_id': '2'
  },
  {
    'song_name': 'Blue Christmas',
    'song_duration': '2:09',
    'artist_id': '2'
  },
  {
    'song_name': 'Santa Bring My Baby Back',
    'song_duration': '1:54',
    'artist_id': '2'
  },  {
    'song_name': 'O Little Town of Bethlehem',
    'song_duration': '2:37',
    'artist_id': '2'
  },
  {
    'song_name': 'Silent Night',
    'song_duration': '2:25',
    'artist_id': '2'
  },
  {
    'song_name': 'Peace in the Valley',
    'song_duration': '3:22',
    'artist_id': '2'
  },  {
    'song_name': 'I Believe',
    'song_duration': '2:05',
    'artist_id': '2'
  },
]
# Elvis albumlista
for mock_elvis in songs_elvis:
  run('INSERT INTO song VALUES(NULL, :artist_id, :song_name, :song_duration)', mock_elvis)





songs_mj = [
  {
    'song_name': 'Bad',
    'song_duration': '4:07',
    'artist_id': '3'
  },
  {
    'song_name': 'The Way You Make Me Feel',
    'song_duration': '4:58',
    'artist_id': '3'
  },
  {
    'song_name': 'Speed Demon',
    'song_duration': '4:01',
    'artist_id': '3'
  },
  {
    'song_name': 'Liberian Girl',
    'song_duration': '3:53',
    'artist_id': '3'
  },
  {
    'song_name': 'Just Good Friends',
    'song_duration': '4:05',
    'artist_id': '3'
  },
  {
    'song_name': 'Another Part of Me',
    'song_duration': '3:53',
    'artist_id': '3',
  },  {
    'song_name': 'Man in the Mirror',
    'song_duration': '5:18',
    'artist_id': '3'
  },
  {
    'song_name': 'I Just Can’t Stop Loving You',
    'song_duration': '4:13',
    'artist_id': '3'
  },
  {
    'song_name': 'Dirty Diana',
    'song_duration': '4:41',
    'artist_id': '3'
  },  {
    'song_name': 'Smooth Criminal',
    'song_duration': '4:16',
    'artist_id': '3'
  },
]
# Michael Jackson
for mock_mj in songs_mj:
  run('INSERT INTO song VALUES(NULL, :artist_id, :song_name, :song_duration)', mock_mj)