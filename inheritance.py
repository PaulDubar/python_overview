# attributes defined in a class can be inherited by another class
# this module uses Chef.py class and Chinese_Chef.py to demonstrate inheritance
#
from Chef import Chef
from Chinese_Chef import ChineseChef

myChef = Chef() # create a local object based on Chef class
myChef.make_chicken() # I can now call this function in my local object

# now use the attributes from Chinese_Chef class

myChineseChef = ChineseChef()
myChineseChef.make_salad() # this function is inherited from Chef
myChineseChef.make_fried_rice() # this function is local to ChineseChef class only