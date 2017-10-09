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

def addPerson():
	name=input('name: ')
	contactWeb.web.addUser(name)
	contactWebInit.data.people[name]={}
	print('Would you like to add a connection? [Y/N]')
	answer=input('>>> ')
	if(answer=='y'):
		addConnection(name)
	
