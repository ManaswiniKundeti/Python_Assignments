# given string "abccde". Print the char that is repeated
s = input("Enter the string :")
dic = {}
for char in s:
	dic[char] = 0
# str = [char for char in s]
# ip = {}.fromkeys(str,0)

# new_ip = {key:(v+1 if k == v else v for k,v in ip.items())for key,value in ip.items()}

# new_ip = {key : (value for value in ip.items() if value in ip.items()) for key,value in ip.items()}


# for char in ip:
# 	ip[letter] += 1
# 	return ip

for char in s:
	dic[char] += 1

for char,count in dic.items():
	if count > 0:
		print(char, count)

# print(ip)
# print(new_ip)