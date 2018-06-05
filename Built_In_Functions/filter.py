names = ["austin","penny","anthony","angel","billy"]

#new list with names that start with 'a'
a_names = filter(lambda n : n[0] == 'a' , names)
start_a_names = list(a_names)

print(start_a_names)