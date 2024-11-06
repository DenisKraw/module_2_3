
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
age = 0
while age < len(my_list):
    for my_list_1 in my_list:
        if age < my_list_1:
            print(my_list_1)
    break
