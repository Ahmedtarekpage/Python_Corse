# names = input("Enter names separated by commas: ").title().split(",")
# assignments = input("Enter assignment counts separated by commas: ").split(",")
# grades = input("Enter grades separated by commas: ").split(",")
#
#
# message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
# submit before you can graduate. You're current grade is {} and can increase \
# to {} if you submit all assignments before the due date.\n\n"
#
# for name, assignment, grade in zip(names, assignments, grades):
#     print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))
#####################################################################################################
# result = 0
# while(result == 0):
#     try:
#         num1= int(input("Enter First Input : "))
#         num2= int(input("Enter Second Input : "))
#         result = num1 / num2
#         print(result)
#
#     except ValueError:
#         print("You Entered incorrect input You have to Enter a Number data type")
#     except ZeroDivisionError:
#         print("You Shouldn't divide by ZERO")
# print("Continue ")
######################################################################################

f = open('saud.txt', 'w')
f.write("This is an additional txt")
f.close()

f = open('a.txt', 'r')
file_data = f.read()
f.close()
print(file_data)
##############################################################################################
