# this file is exercise with tuple

list1 = [1, 2, 3] # list
dict1 = {1, 2, 3}  # dictionary

tuple1 = (1, 2, 3) # tuple

x = 1, 2, 3 # packing

w, y, z = x # unpaking

print('{} + {} + {} = {}'. format(w, y, z, x))

a, b = 1, 2 # this is tuple

print('{} {}'. format(a, b))

a, b = b, a

print('{} {}'. format(a, b))

ages = {'Teddy' : 20, 'Jane' : 25, 'Kale' : 30} # dictionary

for name, age in ages.items():
    print('{}의 나이는: {}' .format(name, age)) # not using tuple
    
print('---------------------------------')
for x in ages.items():
    print('{}의 나이는: {}' .format(x[0], x[1])) # using tuple
    
print('---------------------------------')
for x in ages.items():
    print('{}의 나이는: {}' .format(*x)) # using tuple
