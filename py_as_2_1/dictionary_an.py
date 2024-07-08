import random
import string
def diction(n):
    dicti = {}
    for i in range(n):
        name = "".join(random.choices(string.ascii_letters, k = random.randint(4,10)))
        age = random.randint(18,80)
        dicti[i] =  {"name": name, "age": age}
    return dicti

n = int(input("Enter the length of the dictionary:\n"))
diction(n)
for i in range(n):
    print(diction(n)[i])