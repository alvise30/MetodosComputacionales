# definition of a list with 4 items
my_list = ["Apple\n", 3.40, 1, "Hello world\n"]

# print them one by one
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])

#print the first three
print(my_list[0:3])

#iterate and do something with each item
for item in my_list:
    new_item = 10 * item
    print(new_item)

