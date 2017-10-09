import contactWeb

class Struct(object):pass
data=Struct()

#function takes in data and converts SQL DB into list of dictionaries for
#easier interpretation
def DBtoDict(data):
	data.people=[]
	contactWeb.web.cursor.execute("SELECT Name FROM users")
	result=contactWeb.web.cursor.fetchall()
	for person in result:
		name=person[0]
		personDict={'Name':name}
		for connection in contactWeb.web.cursor.execute("SELECT * FROM %s"%name):
			personDict[connection[0]]=connection[1]
		data.people.append(personDict)

#initializes functions that cannot run during program due to efficiency
def init(data):
	DBtoDict(data)