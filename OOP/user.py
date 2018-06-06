# Using the init method to initialize a class

class User:
	active_users = 0
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

	# def say_hi():
	# 	print("HELLO!!")
print(f"Active Users Before : {User.active_users}")
user1 = User("Joe","Upperla",24)
user2 = User("Sahithi","Khandavalli")
user3 = User("Leela","Sundaram",79)
print(f"Active Users After : {User.active_users}")

print(user1.first_name,user1.last_name)
print(user2.first_name,user2.age)

print(user3.likes("Aviyal"))
print(user1.likes("Shopping"))

print(user2.initials())
print(user3.initials())

print(user3.is_senior())
print(user2.age)
print(user1.birthday())
print(user1.age)
print(user1.logout())
print(f"Active Users Now : {User.active_users}")
#user1.say_hi()  throws error as there is no self parameter in the function definition 