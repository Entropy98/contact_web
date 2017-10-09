import contactWeb
import contactWebInit

def addConnection(person):
	print('Input connection type')
	connType=input('>>> ')
	print('Input connection name')
	name=input('>>>')
	contactWeb.web.addConnection(person,connType,name)
	contactWebInit.data.people[person][connType]=name
	print('Would you like to add another connection? [Y/N]')
	answer=input('>>> ')
	if(answer=='y'):
		addConnection(person)

def addPerson(data):
	name=input('name: ')
	contactWeb.web.addUser(name)
	contactWebInit.data.people[name]={}
	print('Would you like to add a connection? [Y/N]')
	answer=input('>>> ')
	if(answer=='y'):
		addConnection(name)
	
def generateLinks(data):
	data.links={}
	for person in contactWebInit.data.people:
		for connection in contactWebInit.data.people[person]:
			link=(connection,contactWebInit.data.people[person][connection])
			if(link not in data.links):
				data.links[link]=[person]
			else:
				data.links[link].append(person)
	print(data.links)
