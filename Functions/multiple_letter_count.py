'''
multiple_letter_count("awesome") # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}
'''

string_input = input("Enter the string : ")

def multiple_letter_count(str):
	letter_count = {letter : str.count(letter) for letter in str}
	return letter_count

print(multiple_letter_count(string_input))