def printDetails(item, **kwargs):
    print('item name is : ' , item)
    for key , value in kwargs.items():
        print(key, value)

printDetails("Monitor", price =70, Quantity = 85)