def special_greeting(**kwargs):
	print(kwargs)
	if "Manu" in kwargs and kwargs["Manu"] == "special":
		return "You get a special greeting Manaswini!!"
	elif "Manu" in kwargs:
		return f"{kwargs['Manu']} Manaswini!!"

	return "Not sure who this is...."

print(special_greeting(Manu='Hello'))  #Hello Manaswini!
print(special_greeting(Bob='hello'))  #Not sure who this is....
print(special_greeting(Manu = 'special'))  #You get a special greeting Manaswini

print(special_greeting(Sai = "hello",Manu="special"))