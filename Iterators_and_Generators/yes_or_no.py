def yes_or_no():
    answer = "yes"
    while True:
        yield answer
        answer = "no" if answer == "yes" else "yes"


gen = yes_or_no()
print(next(gen)) # 'yes'
print(next(gen)) # 'no'
print(next(gen)) # 'yes'
print(next(gen)) # 'no'
