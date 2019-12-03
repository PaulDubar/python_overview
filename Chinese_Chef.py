# Will inherit from Chef.py instead of duplicating the functions
from Chef import Chef # we need to do this in order to be able to use its attributes

class ChineseChef(Chef): # we are saying that inside this ChineseChef class, we want to be be able to use 
    # all the functions from the Chef class
    def make_fried_rice(self): # this function is specific to the Chinese Chef class
        print("The chef makes fried rice")
    
# so the class ChineseChef has inherited the attributes from Chef plus has its own attributes