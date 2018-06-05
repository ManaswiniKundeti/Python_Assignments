#try: will try to do something
#except: runs if there is an error
#else: runs if there is no error
#finally: runs no matter what at the end

# try:
# 	num = int(input("PLease enter a num :"))
# except:
# 	print("Thats not a number")
# else:
# 	print("I'm in the else")
# finally:
# 	print("Runs!! no matter what!!")

while True:
	try:
		num = int(input("PLease enter a num :"))
	except ValueError:
		print("Thats not a number")
	else:
		print("Good job!! you entered a number!!")
		break
	finally:
		print("Runs!! no matter what!!")
print("REst of game logic runs!!")