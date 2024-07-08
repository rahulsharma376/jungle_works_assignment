import random

def min_max(n):
    i = 0
    minn = maxx = n[i]    #Assign same value to both variable
    while i<len(n):         # will run loop from 0 to [len(n) which is 9]
        if n[i] > maxx:
            maxx = n[i]
        elif n[i] < minn:
            minn = n[i]
        i+=1
    return minn, maxx


n = list(random.randint(1,1000) for _ in range(10))              # randint will return a number and for loop will iterate 10 times. this will create a list.
print(n)                                                         # (above line) _(underscore) is used for indicating that loop variable is not used within loop body.
# ans = min_max(n)
minn, maxx = min_max(n)
print(f"The Greatest number is {maxx}\nThe Smallest number is {minn}")



