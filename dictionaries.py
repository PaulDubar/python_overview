# dictionary is a key, value pair construct
# Retrieval is by specifying the key
# Duplicate keys are no-no
#
monthConversions = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March"
}

print(monthConversions["Feb"]) # or
print(monthConversions.get("Mar")) # use the get function
# if the key doesnt exist, None is returned
print(monthConversions.get("Dec")) 
# .get allows us to provide a default value to be returned if a key is unmapped
print(monthConversions.get("Dec", "Key doesnt exist")) 