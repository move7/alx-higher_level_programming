#!/usr/bin/python3
result = ""
for i in range(1, 100):
    if(i % 15 == 0):
        result += "FizzBuzz"
    elif(i % 5 == 0):
        result += "Buzz"
    elif(i % 3 == 0):
        result += "Fizz"
    else:
        result += str(i)
    result += " "
print(result + "Buzz", end='')
