#check if the input contains all the vowels(aeiou) ! T/F
string = input("String : ")
setd = len({char for char in string if char in 'aeiou'}) == 5
if(setd == True):
	print(f"Hurray!! {string} contains all the vowels")  #sequioa is a plant name that contains all vowels in it
else:
	print(f" Arghh! {string} contains only {len({char for char in string if char in 'aeiou'})} vowels ")
print(setd)