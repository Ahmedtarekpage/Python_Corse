#Tuple  = list → immutable   ordered
my_list = [1,2]
my_tuple = (1,2)
my_tuple2 = 1,2
print(type(my_list))
print(type(my_tuple))
print(type(my_tuple2))
#orderd - Mutable
print(my_list[1])
print(my_tuple[0])

location = (13.4125, 103.866667)
print("Latitude:", location[0])
print("Longitude:", location[1])
#############################################################
m_salary = 10000
print("Saud's Salary = {}  his yearly salary = {} ".format(m_salary, m_salary * 12))
###############################################################
dimensions = 52, 40, 100
print(dimensions)
length, width, height = dimensions
print("The dimensions are {} x {} x {}".format(length, width, height))
##########################################################################
tuple_a = 1, 2
tuple_b = (1, 2)

print(tuple_a == tuple_b)
print(tuple_a[1])

###################################
#set {}
numbers = [1, 2, 6, 3, 1, 1, 6]

unique_nums = set(numbers)
print(numbers)
print(unique_nums)
########################################################
fruit = {"apple", "banana", "orange", "grapefruit"}  # define a set

print("watermelon" in fruit)  # check for element

fruit.add("watermelon")  # add an element
print(fruit)

print(fruit.pop())  # remove a random element
print(fruit)
##############################################################
a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
print(len(a) - len(b))
##############################################################
a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
b.add(5)
b.pop()
print(b)              #yes        No           Maybe
############################################################
# LIST   → Ordered - Mutable
# TUPLE  → Ordered - Immutable
# SET   → Unordered - Mutable
################################################################
# Define a Dictionary, population,
# that provides information
# on the world's largest cities.
# The key is the name of a city
# (a string), and the associated
# value is its population in
# millions of people.

#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5
population =  {'Shanghai': 17.8 ,
               'Istanbul': 13.3 ,
               'Karachi': 13.0 ,
               'Mumbai': 12.5 }
print(population['Shanghai'])
print("1111111111111111111111")
for k in population.keys():
    print(k)
print("222222222222222222222")
for v in population.values():
    print(v)
print("33333333333333333")
for k, v in population.items():
    print(k, v)#############################
animals = {'dogs': [20, 10, 15, 8, 32, 15],
           'cats': [3,4,2,8,2,4],
           'rabbits': [2, 3, 3],
           'fish': [0.3, 0.5, 0.8, 0.3, 1]}
print(animals["fish"][3])

##########################################
VINIX = {'C': [0.74, -6.51],
         'MA': [0.78, 34.77],
         'BA': [0.79, 17.01],
         'PG': [0.85, -8.81],
         'CSCO': [0.88, 18.56],
         'VZ': [0.9, 2.16],
         'PFE': [0.92, 13.96],
         'HD': [0.97, 3.2],
         'INTC': [1.0, 2.61],
         'T': [1.01, -15.19],
         'V': [1.02, 24.0],
         'UNH': [1.02, 19.32]}