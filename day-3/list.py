# list / collection / array

#name1 = "John"
#name2 = "mary"
#name3 = "Sue"

#created variable of names
names = ["John", "Mary", "Sue", "Gary", "RJ"]
# Length to find the amount of characters
print(len(names))

print(names{0}) 
print(names{3}) #gary

#want john and mary [start:end] Sue and Gary [start:end]
print(names[0:2])
print(names {2:4})
print(names{0:3:2})
print(names[0::2]) #Every other item for all of list

#manipulating  list
#names = ["john, "mary", "sue", "gary", "RJ" ]
print(names.append("james")) #add the name to the list.
print(names)

#removing items
(names.remove("Sue") # that will remove sue.
print(names)


#remove by its position
names.pop(0) #that will remove john