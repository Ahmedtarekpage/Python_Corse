# Arithmetic Operators (+ - * /)
print("Arithmetic Operators")
print(2 + 3)
print(5 * 6)
print(2 - 10)
print(5 / 2)
print(5 // 2)
print(2 ** 3)
print(10 % 3)
print("################################################")
#########################################################################
# QUIZ
print("QUIZ")
# My electricity bills for the last three months have been
# $23, $32 and $64. What is the average monthly electricity bill over the three month period?
# Write an expression to calculate the mean, and use print() to view the result.
print(((23 + 32 + 64) / 3))
print("##################################################")
########################################################################################
# Variables
print("Variables")
num1, num2 = 5, 10
print(num1, num2)
# num1 = num1 + 6 → num1 += 6
# num1 = num1 - 5 → num1 -= 5
# num1 = num1 * 2 → num1 *= 2
# num1 = num1 / 2 → num1 /= 2
# num1 = num1 ** 2 → num1 ** 2
# num1 = num1 % 3 → num1 %= 3

num1 += 6
num2 /= 2
print(num1, num2)
# num1 = 5
# num2 = 10
#########################################################
# QUIZ2
print("QUIZ 2")

# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff
rainfall = rainfall * 0.90
rainfall *= .9
print(rainfall)
# add the rainfall variable to the reservoir_volume variable
reservoir_volume += rainfall

# increase reservoir_volume by 5% to account for stormwater that flows
# into the reservoir in the days following the storm
reservoir_volume *= 1.05

# decrease reservoir_volume by 5% to account for evaporation
reservoir_volume *= 0.95

# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.

reservoir_volume -= 2.5e5

# print the new value of the reservoir_volume variable

print(reservoir_volume)
print("########################################")
################################################
print("Data Types ")
x = 5.5
print(type(x))
x = int(x)
print(type(x))
my_inp = int(input("Write a num X 5 : "))
print(my_inp * 5)
print("END")
