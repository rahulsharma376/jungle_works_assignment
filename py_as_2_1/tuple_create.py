import random
import string

num = random.randint(1,500)  #for integer
flt = random.uniform(1.00, 500.00)  #for float
strin = "".join(random.choices(string.ascii_letters, k = random.randint(1,15)))  #for string k for length of ascii letter to select using random choices and creating list and then join with empty string.

tp = (num, flt, strin)
print(tp)