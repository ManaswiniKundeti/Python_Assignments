'''
last_element([1,2,3]) # 3
last_element([]) # None
'''
l = [1,2,3]
m = []
def last_element(l):
    if l:
        return l[-1]
    return None

print(last_element(l))
print(last_element(m))
