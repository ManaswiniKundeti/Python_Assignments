'''
compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]
'''
def compact(l):
    return [val for val in l if val]

print(compact([0,1,2,"",[], False, {}, None, "All done"]))