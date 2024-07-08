def prime_set():
    st = set()
    for i in range(2,11):
        count = 0
        for j in range(2,i):
            if(i%j == 0):
                count+=1
        if count == 0:
            st.add(i)
    return st

print(prime_set())
