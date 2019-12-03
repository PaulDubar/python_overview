phrase = "python is"
phrase = phrase + " cool"
print(phrase.upper())
print(phrase.lower())
print(phrase.isupper())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[0])
print(phrase[-1]) #prints last character
print(phrase[-2]) #etc counting back from -1
#
# Index function
#
print(phrase.index("c")) #return the index of the first occurence of c = 10
print(phrase.index("cool")) #return the index of the start of this pattern
#
# Replace something
#
print(phrase.replace("cool","not cool"))