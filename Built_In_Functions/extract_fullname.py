'''
func should accept a list of dictionaries and return anew list if strings with
first and last name keys in each dictionary concatenated
names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
extract_full_name(names) # ['Elie Schoppik', 'Colt Steele']
'''

def extract_full_name(l):
    return list(map(lambda val: "{} {}".format(val['first'], val['last']), l))

names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]

print(extract_full_name(names))