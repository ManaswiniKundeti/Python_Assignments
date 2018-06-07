class User:
	active_users = 0

	@classmethod
	def display_active_users(cls):
		return f"There are currently {cls.active_users} active users"
	
	def __init__(self,first,last,age=23):
		self.first_name = first
		self.last_name = last
		self.age = age
		User.active_users += 1

	def full_name(self):
		return f"{self.first_name} {self.last_name}"

	def logout(self):
		User.active_users -= 1
		return f"{self.first_name} has logged out"

	def initials(self):
		return f"{self.first_name[0]}.{self.last_name[0]}"

	def likes(self,thing):
		return f"{self.first_name} likes {thing}"

	def is_senior(self):
		return self.age >= 65

	def birthday(self):
		self.age += 1
		return f"Happy {self.age}th Birthday,{self.first_name}"

	
class Moderator(User):
	total_mods = 0
	def __init__(self,first,last,age,community):
		super().__init__(first,last,age)
		self.community = community
		Moderator.total_mods += 1

	@classmethod
	def display_active_mods(cls):
		return f"There are currently {cls.total_mods} active mods"

	def remove_post(self):
		return f"{self.full_name()} removed a post from the {self.community} community"


# print(User.display_active_users())
# u1 = User("Tom","Garcia",35)

# print(User.display_active_users())
# jasmine = Moderator("Jasmine","Conner",63,"Keyboard")
# print(User.display_active_users())

# print(jasmine.full_name())
# print(jasmine.community)

u1 = User("Tom","Garcia",35)
u2 = User("Tom","Garcia",35)
u3 = User("Tom","Garcia",35)
jasmine1 = Moderator("Jasmine","Conner",63,"Keyboard")
jasmine2 = Moderator("Jasmine","Conner",63,"Keyboard")
print(User.display_active_users())
print(Moderator.display_active_mods())


