# list_1 = [1, 2, 3]
# list_2 = [n+1 for n in list_1]
# list_multiplied = [n*2 for n in range(1,5)]

names = ['Angela', 'Pete', 'Jack', 'Josephine', 'Carol', 'Peter', 'Jule']

short_names = [name for name in names if len(name) < 5]
uppercased_names = [name.upper() for name in names if len(name) > 4]

print(short_names)
print(uppercased_names)
