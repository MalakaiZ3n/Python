count = 0
for number in range(1, 1000):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"We have {count} even numbers")
