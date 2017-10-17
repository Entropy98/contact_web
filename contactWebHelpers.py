import contactWeb
import contactWebInit

def addConnection(person):
	print('Input connection type')
	connType=input('>>> ')
	print('Input connection name')
	name=input('>>>')
	contactWeb.web.addConnection(person,connType,name)
	contactWebInit.data.people[person][connType]=name

	link=(connType,contactWebInit.data.people[person][connType])
	if(link not in contactWebInit.data.links):
		contactWebInit.data.links[link]=set([person])
	else:
		contactWebInit.data.links[link]=contactWebInit.data.links[link].union(set([person]))

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
