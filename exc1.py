# Create a function that takes a list as a parameter,
# and returns a new list with all its element's values doubled.
# It should raise an error if the parameter is not a list.

nums = [423, 32, 87, 464, 892]

def doppel(lista):
    newlist = []
    for x in lista:
        if type(lista) != list:
            raise TypeError("not a list, fool!")
        else:
            newlist.append(x*2)
    return newlist

print(doppel(nums))
print(doppel("nums"))
