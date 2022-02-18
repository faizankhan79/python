some_list = ['a' , 'b' , 'c' , 'd' , 'b' , 'e' , 'x' , 'x']
duplicate = []
for item in some_list:
    if some_list.count(item) > 1:
        if item not in duplicate:
            duplicate.append(item)
print('Duplicate =' , duplicate )


duplicate2 = list(set(x for x in some_list if some_list.count(x) > 1))
print(duplicate2)
