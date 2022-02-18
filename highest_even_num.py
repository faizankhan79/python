def highest_even(list):
    even = []
    for value in list:
        if value % 2 == 0:
            even.append(value)
    return max(even)

print(highest_even([10,2,3,4,8,11]))
