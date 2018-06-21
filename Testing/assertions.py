# def add_positive_numbers(x,y):
# 	assert x>0 and y>0,"Both numbers must be positive"
# 	return x+y

# print(add_positive_numbers(1,1)) #2
# print(add_positive_numbers(1,-1)) #assertionEroor : Both numbers must be positive


def eat_junk(food):
	assert food in [
	"pizza",     
	"ice cream",
	"candy",
	"burger",
	"fries"
	] , "Food must be junk food!"
	return f"NOM NOM NOM I am eating {food}"


food = input("Enter a junk food :")
print(eat_junk(food))
