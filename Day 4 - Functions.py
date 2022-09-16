def my_func(a,b) :
    print("Hello")
    print("World ")
    return a*b
x = my_func(2,3)
print(x)

 ######################################333
 #Scope
x = 10

def next():
    global x
    x = 20


print(x)
next()
print(x)

def readable_timedelta(days):
    """Return a string of the number of weeks and days included in days."""
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)

print(readable_timedelta(50))

#################################################################################################
#Lambda
def mu(x):
     return x * 2
x = mu(4)
print(x)


x = lambda x: x*2
x(4)
######################################################################################################
numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

averages = list(map(lambda x: sum(x) / len(x), numbers))
print(averages)

def average(numbers):
    my_list = []
    for i in numbers:
        my_list.append(sum(i) / len(i))
    print(my_list)

average(numbers)
######################################################
# my_list = []
# for i in range(5):
#     my_list.append(i)
# print(my_list)
#

my_list = [i  for i in range(5)]
print(my_list)
test = (1,2,3,4)
my_list = list(map(lambda x: x * 2, test))
print(my_list)
########################################################
#Filter
cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

short_cities = list(filter(lambda x: len(x) < 10, cities))
print(short_cities)
###########################################################3

print(range(5)[0:2])
def chunker(iterable, size):
    """Yield successive chunks from iterable of length size."""
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]

for chunk in chunker(range(25), 4):
    print(list(chunk))