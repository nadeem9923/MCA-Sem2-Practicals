l = [11, 10, 5, 4, 86, 30, 102]

even_count, odd_count = 0, 0

# iterating each number in list
for num in l:

    # checking condition
    if num % 2 == 0:
        even_count += 1

    else:
        odd_count += 1

print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)