set = {88, 95, 65, 81, 45, 45, 79}
set1 = {67, 88, 81, 46, 79}
set2 = {95, 65, 81}
set3 = {65}
set4 = { 58, 63, 45, 9, 4}
beta = {96, 89, 235}
print(set)
set.add(5)#Adds an element to the set. If an element is already exist in the set, then it does not add that element.
print(set)
set.pop()
print(set)
beta.clear()	#Removes all the elements from the set.
print(beta)
set.copy()
print(set)	#Returns a shallow copy of the set.
print("The difference : " , set2.difference(set3))	#Returns the new set with the unique elements that are not in the another set passed as a parameter.
 #print("Difference update : " , set2.difference_update(set3))	#Updates the set on which the method is called with the elements that are common in another set passed as an argument.
set.discard(81) #Removes a specific element from the set.
print(set)	
print(set.intersection(set1))	#Returns a new set with the elements that are common in the given sets.
print("Update :" , set2.intersection_update(set3))	#Updates the set on which the instersection_update() method is called, with common elements among the specified sets.
print("Disjoint : " ,set.isdisjoint(set1))	#Returns true if the given sets have no common elements. Sets are disjoint if and only if their intersection is the empty set.
print("Subset : " , set3.issubset(set2))	#Returns true if the set (on which the issubset() is called) contains every element of the other set passed as an argument.
print(set4.pop())	#Removes and returns a random element from the set.
set.remove(95)
print("Set after removing 95 : " , set)	#Removes the specified element from the set. If the specified element not found, raise an error.
print("Symmetrric difference : " ,set.symmetric_difference(set1))	#Returns a new set with the distinct elements found in both the sets.
 #set.symmetric_difference_update()	#Updates the set on which the instersection_update() method called, with the elements that are common among the specified sets.
print("union of sets : " ,set.union(set1))	#Returns a new set with distinct elements from all the given sets.
  #set.update()	#Updates the set by adding distinct elements from the passed one or more iterables.