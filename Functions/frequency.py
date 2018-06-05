'''
frequency([1,2,3,4,4,4], 4) # 3
frequency([True, False, True, True], False) # 1
'''

def frequency(list_item,search):
    num = list_item.count(search)
    return num

list_input = list(input("Enter the list input : "))
search_input = input("Enter the value to be searched : ")

print(frequency(list_input,search_input))