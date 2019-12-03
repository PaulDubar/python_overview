# dont forget the colons
# below is using boolean values
is_male = False

if is_male:
   print("You are male")
else:
   print("You are not male")

is_male = False
is_tall = False

if is_male or is_tall:
    print("You are male or tall or both")
else:
    print("You are neither male or tall") # this one is actioned

is_male = True
is_tall = False
# if statement will follow if path
if is_male or is_tall:
    print("You are male or tall or both") # this one is actioned
else:
    print("You are neither male or tall")

# AND operator

if is_male and is_tall:
    print("You are male or tall or both")
else:
    print("You are either not male or not tall or both") # this one is actioned

is_male = True
is_tall = True
# if statement will follow if path now
if is_male and is_tall:
    print("You are both male and tall") # this one is actioned
else:
    print("You are either not male or not tall or both")

# elif and not conditions

is_male = True
is_tall = False

if is_male and is_tall:
    print("You are male or tall or both")
elif is_male and not(is_tall):
    print("You are male but not tall") # this one is actioned
else:
    print("You are either not male or not tall or both")