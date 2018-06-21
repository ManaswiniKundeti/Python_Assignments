def count_up_to(max):
	count = 1
	while count <= max:
		yield count
		count += 1


counter = count_up_to(5)

print(next(counter)) # prints '1' as the next() runs only once

for n in counter:    # prints all numbers from '2' till the max as it is a for loop
	print(n)