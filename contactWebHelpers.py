import contactWeb

def addConnection(person):
	print('Input connection type')
	connType=input('>>> ')
	print('Input connection name')
	name=input('>>>')
	contactWeb.web.addConnection(person,connType,name)
	print('Would you like to add another connection? [Y/N]')
	answer=input('>>> ')
	if(answer=='y'):
		addConnection(person)

def addPerson():
	name=input('name: ')
	contactWeb.web.addUser(name)
	print('Would you like to add a connection? [Y/N]')
	answer=input('>>> ')
	if(answer=='y'):
		addConnection(name)
	
