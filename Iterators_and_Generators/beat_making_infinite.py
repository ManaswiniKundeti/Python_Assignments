#create a generator as it can return multile times
def current_beat():
	nums = (1,2,3,4)
	i = 0 
	while True:
		if i >= len(nums):i = 0
			yield nums[i]
			i += 1

cd = current_beat()
print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))


# def play_kick_drum():
# 	if current_beat() == 1:
# 		play_sound()