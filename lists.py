friends = ["Tom", "Paul", "Russ", "Karen", "Chrissy"] # you could put numbers or booleans in here
print(friends[0])
print(friends)
print(friends[-1])
print(friends[1:]) # print from index 1 to end of list
print(friends[1:3]) # print a range of elements
print(len(friends)) # print number of elements in the list i.e 5
#
# Modifying an element
#
friends[1] = "Mike"
print(friends)
#
# List functions
#
lucky_numbers = [4, 8, 15, 16 ,23, 42]
friends = ["Tom", "Paul", "Russ", "Karen", "Chrissy"]
friends.extend(lucky_numbers) # essentially appends the list
print(friends) 
friends.append("Creed") # add an item
print(friends)
#
# insert an element
#
friends.insert(1, "Kelly") # insert at element 1
print(friends)
#
# remove a list value
#
friends.remove("Kelly") # but how do you remove based on position in list?
print(friends)
#
#friends.clear # clear the entire list
#
# pop an item off the list
#
friends.pop() # pop the last element
print(friends)
#
print(friends.index("Russ")) # tell me the index of the value 
#
# Count the number of elements containing a value - no looping necessary!
#
print(friends.count("John")) # zero returned
friends.append("Karen")
print(friends.count("Karen")) # should now be 2 - case sensitive
#
# Sorting
#
lucky_numbers.sort() # this sorts the list in ascending order
print(lucky_numbers)
lucky_numbers.reverse() # this just reverse the order of the list - its not a sort
print(lucky_numbers)
#
# Copy a list to another list
#
friends2 = friends.copy()
#
# How do I know the total number of elements in the list?

