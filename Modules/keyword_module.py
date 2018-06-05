import keyword

def contains_keyword(*args):
    for a in args:
        if keyword.iskeyword(a):
            return True
    return False

print(contains_keyword("hello","bye")) #false
print(contains_keyword("def","alaska","chicken")) #true