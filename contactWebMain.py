import contactWeb

#main
while(contactWeb.web.active):
	#temporary UI using raw input until gui is created
	command=input('>>>')
	if(command=='-a person'):
		name=input('name: ')
		contactWeb.web.addUser(name)
	if(command=='-s users'):
		contactWeb.web.displayUsers()
	if(command=='-q'):
		contactWeb.web.active=False
	if(command=='-d person'):
		name=input('name: ')
		contactWeb.web.deleteUser(name)
	if(command=='-a connection'):
		person=input('person: ')
		connType=input('connection type: ')
		name=input('name: ')
		contactWeb.web.addConnection(person,connType,name)