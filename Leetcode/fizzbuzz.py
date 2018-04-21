# Problem:  412. Fizz Buzz

def fizzBuzz(n):
    output = []
    i = 1
    while i<= n:
        if i % 3 == 0 and i % 5 == 0:
            output.append("FizzBuzz")
        elif i % 3 == 0:
            output.append("Fizz")
        elif i % 5 == 0:
            output.append("Buzz")
        else:
            output.append(str(i))
        i+=1
    return output

# Test cases
fizzBuzz(15)
