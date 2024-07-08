import random
import string

#It is used for searching and updating the name in the dictionary
def updating(nam, lst, n):
    for i in lst:
        if(nam == lst[i]["name"]):
            name = input("Enter the New name:\n")
            lst[i]["name"]= name
            print(f"Name updated \"{name}\"")
            return
    print(f"Given name {nam} not found in the dictionary.")
    
    
#Generating random dictionary with name and score
def diction(n):
    dicti = {}
    for i in range(n):
        name = "".join(random.choices(string.ascii_letters, k = random.randint(4,10)))
        scor = random.randint(18,80)
        dicti[i] =  {"name": name, "score": scor}
    return dicti

n = int(input("Enter the length of the dictionary:\n"))
lst = diction(n)
for i in range(n):
    print(lst[i])

naam = input("Enter the name of the person to update the score:\n")

updating(naam, lst, n)

for i in range(n):
    print(lst[i])