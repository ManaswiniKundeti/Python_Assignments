# unsorted_case :

# def search(seq,v):
# 	for x in seq:
# 		if x == v:
# 			return True
# 	return False

# seq = list(input("Enter input list :"))
# v = input("Enter the value to be searched :")
# print(search(seq,v))

# sorted_case :

seq = list(input("Enter input list :"))
v = input("Enter the value to be searched :") 
l = 0
r = len(seq)-1
print(seq)

def bsearch(seq,v,l,r):
#search for v in seq[l:r] , seq is sorted
	if r-l == 0:
		return False
	mid = (l+r)//2 
	if v == seq[mid]:
		return True
	if v < seq[mid] :
		return (bsearch(seq,v,l,mid))
	else:
		return(bsearch(seq,v,mid+1,r))


print(bsearch(seq,v,l,r))