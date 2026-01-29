n = int(input("enter number of people: "))

count = 0

for i in range(n):
    age = int(input("enter age: "))
    if age >= 18:
        count += 1

print("number of people eligible to vote =", count)
