print("Learning_tuples & sets ")
print("Creating tuple")
videoData = tuple(["Introduction",25,"anotherstr"])
print(videoData)
videoTitle, totalVideotime, junkname = videoData
print(videoTitle)
print(totalVideotime)
print(junkname)
##########################################
print("to print new line in python use \n")
print("\n")
print("Learhning sets")
print("create_list_2_set b=set(a)")
print("create_set_2_list a=list(a)")
print("Set operation are union, intersection and difference")
print("\n\n\n")
print("create a set from a list in python")
setx = set(["hello","how","are","you","how"])
print(setx)
print("sets only print out the uniques values")
sety = set(["how","python","operation"])
print("\n union of sets is given by setA| setb")
print(setx|sety)
print("\n intersection of sets is given by setA&setb")
print(setx&sety)
print("\n difference of sets is given by setA - setb")
print(setx-sety)
print("\n\n\n\n Dictionaries are unordered key value pairs")
print("keys are unique and immutable by values can change")
mybio = {'name' : 'vinty', 'game': 'csgo', 'rank':'silver'}
print(mybio)
print("usually the thing that comes in handy to check if there exist any key in dictionary")
print(mybio.has_key('game'),"True means has key and vice versa")
print("\n: to get keys & values from Dictionaries, use .keys() and .values()")
print("\nkeys in mybio are ",mybio.keys())
print("\nvalues in mybio are ",mybio.values ())
print("\nto get tuples,use  .items()")
print("tuples in mybio are", mybio.items())
print("\n to get particular value from sets use .get(key)")
print("the game i play",mybio.get('game'))
mybio['location'] = 'sf'
print("\n\n\n\nappending in the dictionary")
print(mybio)
print("\n\n deleting key-value pair from Dictionaries-use del dict['key']")
del mybio['game']
print(mybio)
print("\n\n\n:to delete whole dictionary use dictionary use dict.clear()")
mybio.clear()
print(mybio)
print("\n\n\nuse dir() call to check the list to attributes from the interpreter." )
print("your name is " + name)

if name == "one":
	print("you are one")
	print("you are admin")
elif name == "game":
	print("playing csgo")
	print("best game")
else:
	print("i dont know you")
	


#stuying while loop
#  while statement_is_true:
#      do stuff
game_rank =20 

while game_rank > 10:
	game_rank = int(input("enter rank in your favourite game"))
	if game_rank > 10:
		print("you are doing good")
	else:
		print("need to learn game")
	 
	
#for loops in python
names =['csgo','pop','nfsmw','hotpersuit']
for name in names:
	print(name)
	
	
