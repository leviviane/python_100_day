#between 1-100 including 100 if num / 3 it should bring Fizz, num / 5 it should print Fuzz, if both then FizzBuzz

target = 100
for num in range(1, target + 1):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
