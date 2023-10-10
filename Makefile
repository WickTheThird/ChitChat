runBack:
	cd /Users/filipbumbu/Documents/GitHub/ChitChat/chitChatBackend/; python manage.py runserver

runFront:	
	cd /Users/filipbumbu/Documents/GitHub/ChitChat/chitfront/; npm start

installFrontDep:	
	cd /Users/filipbumbu/Documents/GitHub/ChitChat/chitfront/; npm install

installFrontDep:
	cd /Users/filipbumbu/Documents/GitHub/ChitChat/chitChatBackend/; pip install requirements.txt

code:
	code .

.PHONY: runBack installBackDep runFront installFrontDep code

