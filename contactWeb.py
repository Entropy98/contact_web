import sqlite3

class Web(object):
	"""Class contains methods for user interaction with the database.
	Class also initializes connection to database and creates framework for
	interactions."""
	def __init__(self):
		super(Web, self).__init__()
		self.conn=sqlite3.connect('people.db')
		self.cursor=self.conn.cursor()
		self.active=True

	'''Method adds a new person to the users table with an incrementing ID'''
	def addUser(self,name):
		for recentID in self.cursor.execute("SELECT MAX(ID) FROM users"):
			maxID=recentID[0]
			print(recentID)
		if(maxID==None):
			maxID=0
		else:
			maxID=int(maxID)
		ID=maxID+1
		for i in self.cursor.execute('''SELECT Name FROM users WHERE Name
			IN (?)''',(name,)):
			curName=i[0]
			if(name in curName):
				if(len(name)==len(curName)):
					nameInt=1
				else:
					nameInt=int(curName[len(name):])
				name+=str(nameInt)
				
		val=(ID,name)
		self.cursor.execute("INSERT into users VALUES (?,?)",val)
		#create subsidiary table for new user
		web.cursor.execute('CREATE TABLE %s(type text, name text)'%name)
		self.conn.commit()

	'''Method shows all values in the users table'''
	def displayUsers(self):
		for user in self.cursor.execute('SELECT * FROM users'):
			print(user)

	'''Method deletes a row from the users table'''
	def deleteUser(self,name):
		self.cursor.execute("DELETE FROM users WHERE Name=?",(name,))
		for i in self.cursor.execute('''SELECT Name FROM users WHERE Name
			IN (?)''',(name,)):
			curName=i[0]
			if(name in curName):
				if(len(name)==len(curName)):
					nameInt=1
				else:
					nameInt=int(curName[len(name):])
				name+=str(nameInt)
		self.cursor.execute("DROP TABLE %s"%name)
		self.conn.commit()

web=Web()


#main
while(web.active):
	#temporary UI using raw input until gui is created
	command=input('>>>')
	if(command=='-a person'):
		name=input('name: ')
		web.addUser(name)
	if(command=='-s'):
		web.displayUsers()
	if(command=='-q'):
		web.active=False
	if(command=='-d person'):
		name=input('name: ')
		web.deleteUser(name)

