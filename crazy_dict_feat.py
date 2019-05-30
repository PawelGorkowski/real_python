# outcome is {True: 'maybe'} cuz True = 1 = 1.0 as dict is a set
x = {True: 'yes', 1: 'no', 1.0: 'maybe'}

myset = {1, 1.0, True, '1'}
print(myset)
