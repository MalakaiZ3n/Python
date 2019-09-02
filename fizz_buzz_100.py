# print in range 100 multiple 3 and 5

for fizz_buzz in range(100):

    if (fizz_buzz % 3 == 0) and (fizz_buzz % 5 == 0):
        print("FizzBuzz")
        continue

    if fizz_buzz % 3 == 0:
        print("Fizz")
        continue

    if fizz_buzz % 5 == 0:
        print("Buzz")
        continue


print(fizz_buzz)
