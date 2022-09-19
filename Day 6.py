my_list = ["Ahmed ", "Saud"]
my_list.insert(0, "Salah")
del my_list[1]
my_list.append("eiad")
my_list.append("eiad")
my_list.remove("eiad")
print(my_list)
most_recent_user = my_list.pop()
print(most_recent_user)
my_list.reverse()
print(my_list)

numerical_list = list(range(1, 1000))
numerical_list.sort(reverse=True)
print(numerical_list)
names = ['kai', 'abe', 'ada', 'gus', 'zoe']
upper_names = []
for name in names:
    upper_names.append(name.upper())
print(upper_names)

dimensions = (800, 600)
print(dimensions)
dimensions = (1200, 900)
########################################################
my_dic = {"Ich": "I",
          "Auto": "Car "}

print(my_dic["Auto"])
print(my_dic.get("Auto"))

# print(my_dic["Du"])
print(my_dic.get("DU", 100))

alien_0 = {'color': 'green', 'points': 5}
alien_0['x'] = 0
alien_0['y'] = 25
alien_0['speed'] = 1.5
print(alien_0)

users = []
# Make a new user, and add them to the list.
new_user = {
    'last': 'fermi',
    'first': 'enrico',
    'username': 'efermi',
}
users.append(new_user)
# Make another new user, and add them as well.
new_user = {
    'last': 'curie',
    'first': 'marie',
    'username': 'mcurie',
}
users.append(new_user)
print(users)

# Show all information about each user.
for user_dict in users:
    for k, v in user_dict.items():
        print(k, v)
    print()

squares = {x : x**2 for x in range(5)}
print(squares)

group_1 = ['kai', 'abe', 'ada', 'gus', 'zoe']
group_2 = ['jen', 'eva', 'dan', 'isa', 'meg']
my_dic = {x:y for x, y in zip(group_1, group_2)}
print(my_dic)
####################################################
my_list = ["fdsafgdesa"]
if my_list:
    print("X")
#############################
def summ(x = 2, y = 3):
    print(x + y)

summ(10, 4)

#########################
def make_pizza(size, *toppings):
 """Make a pizza."""
 print(type(toppings))
# Make three pizzas with different toppings.
make_pizza('small', 'pepperoni')
make_pizza('large', 'bacon bits', 'pineapple')
make_pizza('medium', 'mushrooms', 'peppers',
 'onions', 'extra cheese')
######################################################################################
def build_profile(first, last, **user_info):
 """Build a dictionary for a user."""
 user_info['first'] = first
 user_info['last'] = last
 return user_info


# Create two users with different kinds
# of information.
user_0 = build_profile('albert', 'einstein',
 location='princeton')
user_1 = build_profile('marie', 'curie',
 location='paris', field='chemistry')
print(user_0)
print(user_1)

