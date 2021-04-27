import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
	CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
	if not line.startswith('From: '): continue
	pieces = line.split()
	email = pieces[1]
	# The question mark here is the place holder, avoiding the sql injection
	# We can have many ? and use the tuple to give the data needed
	cur.execute('SELECT count FROM Counts WHERE email = ?', (email,))
	row = cur.fetchone()
	# If the current record is not exist, add a new one, otherwise increase the count
	if row is None:
		cur.execute('''INSERT INTO Counts (email, count) 
			VALUES (?, 1)''', (email,))
	else:
		cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
			(email,))
	# Write to the data on disk, this is the slow part
	conn.commit()

sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
	print(str(row[0]), row[1])
cur.close()