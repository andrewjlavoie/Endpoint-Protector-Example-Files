import random

def generate_ssn():
    print(str(random.randint(0,9)) + \
        str(random.randint(0,9)) + \
        str(random.randint(0,9)) + \
        '-' + \
        str(random.randint(0,9)) + \
        str(random.randint(0,9)) + \
        '-' + \
        str(random.randint(0,9)) + \
        str(random.randint(0,9)) + \
        str(random.randint(0,9)) + \
        str(random.randint(0,9)))

for n in range(100):
    generate_ssn()
    print('\n')