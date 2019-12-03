# Similar to a list BUT tuples are IMMUTABLE. contents cannot be modified
# pairs of values in parentheses, whereas lists are in square brackets
#
#
coordinates = (4, 5)
print(coordinates) # print entire tuple content
print(coordinates[0]) # print by index position
#
print(coordinates[0:]) # print all from index position
#
# You can create a list containing pairs of values, but because its a list, it is modifiable
#
coordinates2 = [(4, 5), (6, 7), (8, 9), (10, 11)]
print(coordinates2)
#
# Now element 0 is a pair of values
#
print(coordinates2[0]) # prints (4, 5)
# but you CAN modify the elements in the list
#
coordinates2[0] = (1, 2)
#
print(coordinates2)