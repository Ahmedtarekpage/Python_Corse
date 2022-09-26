# Python code to demonstrate namedtuple()
# Class → only store Data - X Methods
#Methods

from collections import namedtuple

# Declaring namedtuple()
Student = namedtuple('Student', ['name', 'age', 'DOB'])

# Adding values
S = Student('Nandini', '19', '2541997')
mohammed = Student("Mohammed", '22', '25652625')
# Access using index
print("The Student age using index is : ", end="")
print(S[1])

# Access using name
print("The Student name using keyname is : ", end="")
print(S.name)

print(mohammed.name)
print(mohammed[0])
