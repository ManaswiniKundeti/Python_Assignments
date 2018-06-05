'''
is_palindrome('testing') # False
is_palindrome('tacocat') # True
is_palindrome('hannah') # True
is_palindrome('robert') # False
is_palindrome('amanaplanacanalpanama') # True
'''

def is_palindrome(string):
    stripped = string.replace(" ", "")
    if stripped == stripped[::-1] :
    	return "Is a Palindrome"
    else:
    	return "Is not a palindome"

string_input = input("Enter the input string:")
print(is_palindrome(string_input))