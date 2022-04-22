def fizzbuzz(n):
    new_array = []
    for i in range(1, n + 1):
        if (i % 3 == 0) and (i % 5 == 0):
            new_array.append("FizzBuzz")
        elif i % 3 == 0:
            new_array.append("Fizz")
        elif i % 5 == 0:
            new_array.append("Buzz")
        else:
            new_array.append(i)
    print(new_array)
    return new_array


fizzbuzz(15)

