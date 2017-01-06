#! /usr/local/bin/python3
print("this script will show the use of dict in python")
dict = {'game1':'red5','game2':'mw','game3':'csgo','game4':'pop'}
print(dict['game1'])
#creating a new dict and then adding in values

games = {}
games['fps'] = 'csgo'
games['racing'] ='nfsmw'
games['horror'] = 'evil within'
print(games)


print('Updating a dictionary')
#updating value of game two in dict
print("value of game one",dict['game1'])

print("Value of game2",dict['game2'])
dict['game2'] = "not playing" #updating dict value
print("value of game2","dict['game2'])

#deleting dictonary elements
