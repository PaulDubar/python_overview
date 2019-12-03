# for every letter in the collection do something
for character in "This is pythion 101":
    print(character)
#
# now iterate over a list
#
for friend in ["John", "Paul", "Ringo", "George"]:
    print(friend)
# 
# or over a variable
#
friends = ["John", "Paul", "Ringo", "George"]
for friend in friends:
    print(friend)
#
# range function
#
for index in range(10):
    print(index)
# range starts at 3 ends with 9
for index in range(3,10):
    print(index)
#
# use range with a list
# len function returns number of elements in a list
#
for index in range(len(friends)):
    print(index) # not very useful. Prints 0 1 2 3
#
# but now use the index to print the actual element in the list
#
for index in range(len(friends)):
    print(friends[index]) # index contains each positional number of a list item

# build and exponent function - raise to power of
# using a for loop

def raise_to_power(base, power):
    result = 1
    for index in range(power):   # use range to control the iteration of the for loop
        result *= base           # range only works with integer so cant accept float
    return(result)

base = int(input("Enter the base: ")) # range only works with integer so cant accept float
power = int(input("Enter the power up: "))
print(raise_to_power(base, power))