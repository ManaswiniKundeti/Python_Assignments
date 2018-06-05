'''
capitalize("tim") # "Tim"
capitalize("matt") # "Matt"
'''
def capitalize(string):
    return string[:1].upper() + string[1:]

string_input = input("Enter the input string:")
print(capitalize(string_input))