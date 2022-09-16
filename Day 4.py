answer = 35
guess = 35   # this is just a sample answer and guess

if guess < answer:
    result = "Oops!  Your guess was too low."
elif guess > answer:
   result = "Oops!  Your guess was too high."
elif guess==answer:
    result = "Nice!  Your guess matched the answer!"
print(result)

if 5 > 3 :
    print("ahmed")
if 5 > 4 :
    print("sAUD ")


if not (5 > 3 ):
    print("ahmed")
elif 5 > 4 :
    print("sAUD ")

#################################################
#For Loop
print(range(5))
sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]
for i in range(50,25 , -2):
    print(i)
for word in sentence:
    print(word)

for i in range(len(sentence)):
    print(i)
    print(sentence[i])

for i, word in enumerate(sentence):
    print(word, i)
######################################################
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# should create the list:
new_list = []
for word in names:
    # replace space with _
    text = word.replace(" ", "_")

    #lower case function
    text = text.lower()
    # append to empty list
    new_list.append(text)

print(new_list)
    #print new list
usernames = ["joey_tribbiani", "monica_geller", "chandler_bing", "phoebe_buffay"]

##################################################
# <ul>
# <li>first string</li>
# <li>second string</li>
# </ul>
print("<ul>")
for block in usernames :
    print("<li>", block, "</li>")
print("</ul>")
################################################
# cast = {
#            "Jerry Seinfeld": "Jerry Seinfeld",
#            "Julia Louis-Dreyfus": "Elaine Benes",
#            "Jason Alexander": "George Costanza",
#            "Michael Richards": "Cosmo Kramer"
#        }

cast = {}
for i, value in enumerate(usernames):
    cast[names[i]] = value

print(cast)
#####################################################################
# number to find the factorial of
number = 6
# start with our product equal to one
product = 1
# track the current number being multiplied
current = 1

while  current <= number:
    # multiply the product so far by the current number
    product *= current
    # increment current with each iteration until it reaches number
    current += 1


# print the factorial of number
print(product)
##############################################
start_num = 5
end_num = 100
count_by = 2

break_num = start_num
while break_num < end_num:
    break_num += count_by

print(break_num)
##################################################
for j in range(10):
    if j == 6:
        continue
    print(j,end = " ")


print()

for i in range(5):
    print(i,end= " ")
####################################################################################
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break

print(news_ticker)
###############################################################################
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
for point in zip(labels, x_coord, y_coord, z_coord):
    points.append("{}: {}, {}, {}".format(*point))

print(points)
######################################################