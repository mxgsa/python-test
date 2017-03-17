import itertools

r=itertools.imap(lambda x, y: x * y, [10, 20, 30])
print r

for y in r:
    print y

