# 4.3
for i in range(1,21):
    print(i)
# 4.4
numbers = list(range(1,1000001))

# 4.5
print(max(numbers))
print(min(numbers))
print(sum(numbers))

# 4.6
numbers= list(range(1,21,2))
for number in numbers:
    print(number)

# 4.7
numbers = list(range(3,31,3))
for number in numbers:
    print(number)

# 4.8
numbers = list(range(1,11))
for number in numbers:
    number=number**3
    print(number)

# 4.9
cube = [value**3 for value in range(1,11)]
print(cube)