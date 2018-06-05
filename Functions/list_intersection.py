def intersection(list1,list2):
     return [val for val in set(list1) & set(list2)]

list_inp1 = list(input("Enter the list1 : "))
list_inp2 = list(input("Enter the list2 : "))
print(intersection(list_inp1,list_inp2))



# also valid solution:
# def intersection(l1, l2):
#     return [val for val in l1 if val in l2]