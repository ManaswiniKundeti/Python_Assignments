age = 2
# 2-8 $2 ticket
# >65 $5 ticket
# others $10

if not ((age >= 2 and age <= 8) or age >= 65):
	print("You pay $10 and are not a child or senior citizen")
else:
	print("You are child or Senior")