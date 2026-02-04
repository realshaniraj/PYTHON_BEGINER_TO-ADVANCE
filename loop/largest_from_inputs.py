n = int(input("enter total numbers: "))

num = int(input("enter number: "))
largest = num

for i in range(n - 1):
    num = int(input("enter number: "))
    if num > largest:
        largest = num

print("largest number =", largest)
