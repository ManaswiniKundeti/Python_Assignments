# I have two lists, to hold the true and false values
# I loop through the list, calling fn  with each value in the list
# If the result is True, I append the value to the trues  list
# Otherwise, I append the value to the falses  list
# At the end I return a list that contains both the trues  and falses  lists

# def partition(lst, fn):
#     trues = []
#     falses = []
#     for val in lst:
#         if fn(val):
#             trues.append(val)
#         else:
#             falses.append(val)
#     return [trues, falses]



# Using a list comprehension, you can get this function down to a single line.  
def isEven(num):
    return num % 2 == 0

def isOdd(num):
	return num %2 != 0

def partition(lst, fn):
    return [[val for val in lst if fn(val)], [val for val in lst if not fn(val)]]


print(partition([1,2,3,4], isEven))
