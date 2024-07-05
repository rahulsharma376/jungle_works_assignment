n = int(input("Enter the height of triangle:\n"))
for i in range(n,0,-1):
    print(" "*(n-i)+"*"*(2*i-1))