def details(item, components):
    print("The item is : ", item )
    for c in components:
        print('- ', c)


it = input("Enter item name : ")

print('Type yes to exit ')

comp = []
length = 1
i = 0

while i < length:

    c = input("enter components : ")
    if c == 'yes':
        break
    comp.append(c)

    length += 1



details(it , comp)

