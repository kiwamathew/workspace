# A program that calculates the squares of numbers in a list using the map function.
def square(n):
    
    return n**2

# my_list = [1,2,3,4,5,6,7,8]

result = map(square, [1,2,3,4,5,6,7,8])
print(result)
print(list(result))