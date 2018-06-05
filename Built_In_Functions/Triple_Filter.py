'''
function should accept list of numbers, filter out every number that is 
not divisible by 4 and return a new list where every remaining number is tripled
triple_and_filter([1,2,3,4]) # [12]
triple_and_filter([6,8,10,12]) # [24,36]
'''

def triple_and_filter(li):
    return list(filter(lambda s : s % 4 == 0,map(lambda t : t*3,li)))
    
print(triple_and_filter([4,8,5,12,24,9,3]))