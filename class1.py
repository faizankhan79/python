class cat:
    species = 'mammal'
    def __init__(self,name,age):
        self.name = name
        self.age = age

lodu = cat('lodu',2)
bhosdu = cat('bhosdu',3)
gandu = cat('gandu',5)

def oldest_cat(*args):
    return max(args)

print(f'The oldest cat is {oldest_cat(lodu.age , bhosdu.age , gandu.age)} years old.')
