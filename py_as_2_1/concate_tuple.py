import random
import string

def num():    return random.randint(1,500)  #for integer
def flt():    return random.uniform(1.00, 500.00)  #for float
def strin():    return "".join(random.choices(string.ascii_letters, k = random.randint(1,15)))  #for string k for length of ascii letter to select using random choices and creating list and then join with empty string.

tp1 = (num(), flt(), strin())
tp2 = (flt(), strin(), num())
tp = tp1 + tp2
print(tp)