N = int(input("Введіть кількість елементів масиву: "))
array = []
for i in range(N):
    num = int(input(f"Введіть елемент {i+1}: "))
    array.append(num)

sum_positive_multiple_of_3 = 0
for num in array:
    if num > 0 and num % 3 == 0:
        sum_positive_multiple_of_3 += num

print("Сума додатніх елементів, кратних 3:", sum_positive_multiple_of_3)
