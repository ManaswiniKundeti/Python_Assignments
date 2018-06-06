#Class with attributes  -- name : fluffy , species : dog
class Pet:
	allowed_pets = ['cat','dog','fish','rabbit']
	def __init__(self, name, species):
		if species not in Pet.allowed_pets:
			raise ValueError(f"You can't have a {species} pet!!")
		self.name = name
		self.speies = species

	def set_species(self, species):
		if species not in Pet.allowed_pets:
			raise ValueError(f"You can't have a {species} pet!!")
		self.species = species

cat = Pet("Blue","cat")
dog = Pet("Husky","dog")
# crocodile = Pet("Tony","crocodile")

print(cat.name)
# print(crocodile.species)
# we can change the dog species to tiger
# dog.species = "tiger" .... to stop the user from chnaging the species value to whatever he likes,
# we created a method called set species where the user can reset the species value only from the allowed values
