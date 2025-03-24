def add(*numbers):
    total = 0
    
    for num in numbers:
        
        total += num
    return total

print(add(1,2,3,4))