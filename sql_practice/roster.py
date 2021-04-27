import sqlite3

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Tracks')
cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')

conn.close()

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)',
	('Thunderstruck', 20))
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)',
	('My Way', 15))
conn.commit()

print('Tracks')
cur.execute('SELECT title, plays FROM Tracks')
print(cur.rowcount)
#print(cur.fetchone())
for row in cur:
	print(row)

cur.execute('DELETE FROM Tracks WHERE plays < 100')
conn.commit()

cur.execute('SELECT * FROM Tracks')
print(cur.rowcount)
cur.close()

