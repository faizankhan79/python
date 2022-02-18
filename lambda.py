# square my_list
my_list = [1,4,5]
print(list(map(lambda item: item**2 , my_list)))

# sorting list
a = [(0,2) , (4,3) , (9,9) , (10,-1)]
a.sort(key=lambda x: x[1])
print(a)
