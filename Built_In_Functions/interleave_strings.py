def interleave(s1,s2):
    return ' '.join(' '.join(x) for x in (zip(s1,s2)))

print(interleave(['hi','how'],['Madam','are you?']))