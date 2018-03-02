#Just a default database, this is made by myself.
dataBase = [ ['a','b','c'] , ['e','c','a','f'] , ['b' ,'a'] , ['f','b','c'] ]
f0 = ['a','b','c','d','e']
fSet = [ ]
cSet = [ ]

#First time using hashs, sorry if i mess something up.
cMap = {}

#We need to get the individual items in every set and check add it to our table if we don't have it already.
#Also, this will tell us how many times an element pops up. So 'e' shows up once, 'a' shows up 3 times
for givenSet in dataBase :
	for e in givenSet :
		i = 0
		if e not in cMap.keys() :
			cMap[e] = cMap[e] = i
			i = i +1
		if e in cMap.keys() :
			cMap[e] = cMap[e] + 1

#print(cMap)
f1 = {item:cMap[item] for item in cMap if cMap[item] != 1}

#print(f1)

k1 = f1.keys()
fSet.append(f1)
#print(fSet)
fk = cMap
k = 2
finalBase = fSet
while(len(fk) != 0) :
	finalBase.append(fk)
	fk = {item:cMap[item] for item in cMap if cMap[item] > k}
	k = k + 1
	print(finalBase)

