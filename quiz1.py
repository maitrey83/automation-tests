y = []
maxi = []
x = []
listing = []
def collatz(value):
    number = value
    x = [value]
    if value < 1:
        return []
    while value > 1:
        if value%2 == 0:
            value = value/2
        else:
            value = 3*value + 1
        x.append(value)
    length = len(x)
    y.append(length)
    #print(y)
    maximum_value = max(y)
    set = [number, maximum_value]
    highest_value = set[1]
    print(highest_value)
    return set[1]



#for numbers in range(2, 10):

for numbers in range(10000):
    #print('Number ', numbers)
    collatz(numbers)





