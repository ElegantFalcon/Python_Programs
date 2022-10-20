# list are mutable(changeable)


num = [1, 2, 3, 4, 5]
print(num[0])
random = [1, 2, 'hi', 'Whats up', 100]
print(len(random))
print(max(num))
alpha = ['a', 'i' , 'b' , 'x']
print(min(alpha))
num[0] = 'a'
print(num)
num.append(9) # to add new element at the end of a list
print(num)
print(num.count(3)) #to count number of same values
num.extend(alpha) # to combine two list
print(num)
print(num.index('a')) # lowest index of an element
num.insert(1,5)
print(num)
num.pop(5) # removes an element by specifying index. Here 5 is INDEX
print(num)
num.remove(5) # removes the element 5
print(num)
random.reverse()
print(random)
num1 =[6, 56, 778 , 9, 123]
alpha.sort()
print(alpha)
beta =[ 1, 3, 3, 5]
zeta = [5, 6, 3, 7]
beta.clear()
print(beta) # clear all elements
del beta
print(beta)       