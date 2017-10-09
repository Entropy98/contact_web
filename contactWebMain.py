import contactWeb
import contactWebInit
import contactWebHelpers

def main():
	while(contactWeb.web.active):
		#temporary UI using raw input until gui is created
		command=input('>>>')
		#add objects
		if(command=='-a person'):
			contactWebHelpers.addPerson(contactWebInit.data)
		if(command=='-a connection'):
			print('Input name of person')
			person=input('>>> ')
			contactWebHelpers.addConnection(person)
		#delete objects
		if(command=='-d person'):
			print('Input name of person')
			name=input('>>> ')
			contactWeb.web.deleteUser(name)
			contactWebInit.data.people.pop(name,None)
		if(command=='-d connection'):
			print('Input name of person')
			person=input('>>> ')
			print('Input connection type')
			connType=input('>>> ')
			contactWeb.web.deleteConnection(person,connType)
			contactWebInit.data.people[person].pop(connType,None)
		#display objects
		if(command=='-s users'):
			contactWeb.web.displayUsers()
		if(command=='-s connection'):
			print('Input name of person')
			person=input('>>> ')
			contactWeb.web.displayConnections(person)
		if(command=='-s peopleDict'):
			print(contactWebInit.data.people)
		#test commands
		if(command=='-t links'):
			contactWebHelpers.generateLinks(contactWebInit.data)
		#quit
		if(command=='-q'):
			print('Bye!')
			contactWeb.web.active=False

contactWebInit.init(contactWebInit.data)
main()