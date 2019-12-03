# 2D list is a list containing lists
#
number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
# print a 2d list element
#
print(number_grid[0][0]) # from list 0, print the first element in number_grid
#
for row in number_grid:
    print (row) # print each list out in number_grid

for row in number_grid:
    for col in row:
        print(col) # print each individual item, each on its own line
#
#1
#2
#3
#4
#5
#6
#7
#8
#9
#0
#
