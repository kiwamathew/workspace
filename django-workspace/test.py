#print('Hello World!')

def add(*num):
    for i in num:
        
        sum = i + sum
        i = sum 

    return sum

print(add(2,3))
    