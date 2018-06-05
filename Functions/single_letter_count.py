'''
single_letter_count("Hello World", "h") # 1
single_letter_count("Hello World", "z") # 0
single_letter_count("HelLo World", "l") # 3
'''

s1 = input("Enter string :")
c1 = input("Enter the char :")
def single_letter_count(str1,str2):
	ab = str1.lower().count(str2.lower())
	return ab

print(single_letter_count(s1,c1))