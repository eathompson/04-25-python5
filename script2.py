d = {'a':1, 'b':2, 'c':3}

keys = list(d.keys()) #get keys as a list
keys.sort() #sort the keys
for key in keys: #loop in order
    print(key, "maps to", d[key]) #print the values

for value in d.values(): #loop just the values
    print(value)

for key, value in d.items(): #list of tuples!
    print(key, 'maps to', value)

for item in d.items(): #list of tuples!
    print(item)