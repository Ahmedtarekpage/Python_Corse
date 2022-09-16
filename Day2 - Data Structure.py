#LIST → Ordered - Mutable
#TUPLE
#SET
#Dict

#order        #Mutable

#LIST
my_list = [1, 2 ,3 ,4, 6 ,8 ,7, 5 , 130]
print(my_list[2:7])
my_list[1] = 1000
print(my_list)

print(len(my_list))
print(max(my_list))
print(min(my_list))

print(sorted(my_list))
my_list = sorted(my_list)
print(my_list)

new_str = "#".join(["fore", "aft", "starboard", "port"])
print(new_str)
my_list = new_str.split('#')
print(my_list)

my_list.append("Alexandria")
print(my_list)

############################################
a = [1, 5, 8]
b = [2, 6, 9, 10]
c = [100, 200]

print(max([len(a), len(b), len(c)]))
print(min([len(a), len(b), len(c)]))

#############################################
names = ["Carol", "Albert", "Ben", "Donna"]
print(" & ".join(sorted(names)))
############################################
names = ["Carol", "Albert", "Ben", "Donna"]
names.append("Eugenia")
print(sorted(names))
print(names)

############################################################
