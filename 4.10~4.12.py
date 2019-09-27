food = ['pizza','falafel','carrot','cannoli','ice cream']
my_food_1 = food[0:3]
for i in my_food_1:
    print('The first three items in the list are: ' + i)

my_food_2 = food[1:4]
for i in my_food_2:
    print('three items from the middle of the list are: ' + i)

my_food_3 = food[-3:]
for i in my_food_3:
    print('The last three items in the list are: ' + i)

pizza = ['potato','fruit','bacon']
friend_pizzas = pizza[:]
print(friend_pizzas)
pizza.append('durian')
print(pizza)
friend_pizzas.append('chicken')
print(friend_pizzas)
for i in pizza:
    print(i)
for i in friend_pizzas:
    print(i)