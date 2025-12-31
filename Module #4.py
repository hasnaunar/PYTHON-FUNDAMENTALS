#Create a list
thislist = ["apple", "banana", "cherry"]
print(thislist)

#Add an item at the end using append()
thislist.append("orange")
print(thislist)

#Insert an item at a specific position (index 2)
thislist.insert(2, "mango")
print(thislist)

#Create another list
tropical = ["mango", "pineapple"]

#Add elements of tropical list to thislist using extend()
thislist.extend(tropical)
print(thislist)

#Remove a specific item by name
thislist.remove("banana")
print(thislist)

#Remove an item using index number (index 2)
thislist.pop(2)
print(thislist)

#Delete the first item (index 0)
del thislist[0]
print(thislist)

#Remove all items from the list
thislist.clear()
print(thislist)
