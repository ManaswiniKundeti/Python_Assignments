# Using the init method to initialize a class

class User:
	active_users = 0

	@classmethod
	def display_active_users(cls):
		return f"There are currently {cls.active_users} active users"

	@classmethod
	def from_string(cls,data_str):
		first_name,last_name,age = data_str.split(",")
		return cls(first_name,last_name,int(age))

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


# user1 = User("Joe","Upperla",24)
# user2 = User("Sahithi","Khandavalli")
# user3 = User("Leela","Sundaram",79)
# print(f"Active Users : " +User.display_active_users())

manu = User.from_string("Manaswini,Kundeti,24")
print(manu.first_name)
print(manu.full_name())
print(manu.birthday())
