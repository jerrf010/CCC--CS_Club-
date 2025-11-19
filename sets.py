someSet = {0, 1, 2, 3, 4, 5}
someSet2 = {4, 5, 6, 7, 8, 9}

someSet.union(someSet2)  # Combines both sets, removing duplicates
someSet.update(someSet2)  # Adds elements from someSet2 to someSet
someSet3 = someSet.intersection(someSet2)  # Elements common to both sets
someSet3 = someSet.difference(someSet2)  # Elements in someSet but not in some
someSet3 = someSet.symmetric_difference(someSet2)  # Elements in either set but not both

print(someSet)
print(someSet3)
print(someSet2)