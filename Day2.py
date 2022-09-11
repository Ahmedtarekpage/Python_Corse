#Boolean
san_francisco_pop_density = 500
rio_de_janeiro_pop_density = 1000
print(san_francisco_pop_density > rio_de_janeiro_pop_density)
#################################################################
#Strings
print("Ahmed ")
print('Ahmed')
print(' Ahmed Said " Hello "')
print("Ahmed's Car")

ford_quote = 'Whether you think you can, or you think you can\'t--you\'re right.'
print(ford_quote)
# TODO: Fix this string!
ford_quote = "Whether you think you can, or you think you can't--you're right."
username = "Ahmed"
url = "AWASISScience"
timestamp = "12:00:00"
message = username + " accessed the site " + url + " at " + timestamp + "."
print(message)
print(len(username))
########################################################
#QUIZ
# Quiz: Total Sales
# In this quiz, you’ll need to change the types of the input and output data in order
# to get the result you want.
#
# Calculate and print the total sales for the week from the data provided.
# Print out a string of the form "This week's total sales: xxx", where xxx will be the actual total of all the numbers. You’ll need to change the type of the input data in order to calculate that total.
mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

#TODO: Print a string with this format: This week's total sale
# You will probably need to write some lines of code before the print statement.
total = int(mon_sales) + int(tues_sales) + int(wed_sales) + int(thurs_sales) + int(fri_sales)
print("This week's total sales: " + str(total))
##########################################################################################################
print("Hello \n AHmed")

text = "Welcome-to my Website"
x = text.split('-')
print(x[1])
#######################################################################
verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(len(verse))
x=verse.count('you')
print(x)
# Use the appropriate functions and methods to answer the questions above
# Bonus: practice using .format() to output your answers in descriptive messages!