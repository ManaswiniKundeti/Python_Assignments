def show_information(first_name = "Sai" , is_instructor = False):
	if first_name == "Sai" and is_instructor:
		return "Welcome back instructor Sai!!"
	elif first_name == "Sai":
		return "I really thought you were an instructor..."
	return f"Hello {first_name} !"

print(show_information())
print(show_information(is_instructor = True))
print(show_information("Manaswini"))