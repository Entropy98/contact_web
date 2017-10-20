import contactWeb

class Struct(object):pass
data=Struct()

#function takes in data and converts SQL DB into list of dictionaries for
#easier interpretation
def DBtoDict(data):
	data.people={}
	contactWeb.web.cursor.execute("SELECT Name FROM users")
	result=contactWeb.web.cursor.fetchall()
	for person in result:
		name=person[0]
		personDict={}
		for connection in contactWeb.web.cursor.execute("SELECT * FROM %s"%name):
			personDict[connection[0]]=connection[1]
		data.people[name]=personDict

def generateLinks(data):
	data.links={}
	for person in data.people:
		for connection in data.people[person]:
			link=(connection,data.people[person][connection])
			if(link not in data.links):
				data.links[link]=set([person])
			else:
				data.links[link]=data.links[link].union(set([person]))

#initializes functions that cannot run during program due to efficiency
def init(data):
	DBtoDict(data)
	generateLinks(data)