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
		if(maxID==None):
			maxID=0
		else:
			maxID=int(maxID)
		ID=maxID+1
		baseName=name
		for i in self.cursor.execute('SELECT Name FROM users'):
			curName=i[0]
			if(baseName in curName):
				if(len(curName[len(baseName):])>0):
					curNameInt=int(curName[len(baseName):])
				else:
					curNameInt=0
				nameInt=0
				if(len(baseName)==len(curName)):
					nameInt=1
				elif(nameInt<=curNameInt):
					nameInt=curNameInt+1
				name=baseName+str(nameInt)
				
		val=(ID,name)
		self.cursor.execute("INSERT INTO users VALUES (?,?)",val)
		#create subsidiary table for new user
		web.cursor.execute('CREATE TABLE %s(type text, name text)'%name)
		self.conn.commit()

	def addConnection(self,person,connType,name):
		val=(connType,name)
		self.cursor.execute("INSERT INTO %s VALUES (?,?)"%person,val)
		self.conn.commit()

	'''Method shows all values in the users table'''
	def displayUsers(self):
		for user in self.cursor.execute('SELECT * FROM users'):
			print(user)

	def displayConnections(self,person):
		for connection in self.cursor.execute('SELECT * FROM %s'%person):
			print(connection)

	'''Method deletes a row from the users table'''
	def deleteUser(self,name):
		self.cursor.execute("DELETE FROM users WHERE Name=?",(name,))
		self.cursor.execute("DROP TABLE %s"%name)
		self.conn.commit()

	def deleteConnection(self,person,connType):
		self.cursor.execute("DELETE FROM %s WHERE type=?"%person,(connType,))
		self.conn.commit()

web=Web()




