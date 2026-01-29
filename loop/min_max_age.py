n = int(input("enter number of people: "))

age = int(input("enter age: "))
min_age = age
max_age = age

for i in range(n - 1):
    age = int(input("enter age: "))
    if age < min_age:
        min_age = age
    if age > max_age:
        max_age = age

print("youngest age =", min_age)
print("oldest age =", max_age)
