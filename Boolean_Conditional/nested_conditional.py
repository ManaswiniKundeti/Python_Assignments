#ask for age
age = input("How old are you?")

if age:
	age =int(age) 
	if age >= 18 and age < 21 :
		#18-21 wristband
		print("You can enter, but need a wrist band!")
	elif age >= 21:
		#21+ drink and normal entry
		print("You are good to enter and can drink")
	else:
		#too young , sorry
		print("You cant come in, little one!! :( ")
else:
	print("PLease enter an age!!")
