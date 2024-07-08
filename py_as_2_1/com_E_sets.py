import random

def sts():
    st = set()
    for i in range(10):
        st.add(random.randint(1,100))
    return st

def compare(st1, st2):
    i = 0
    st3 = set()
    for i in st1:
        for j in st2:
            if i == j:
                st3.add(i)
    return st3

st1 = sts()
st2 = sts()
print(f"First set: {st1}")
print(f"Second set: {st2}")
print(f"Common set: {compare(st1, st2)}")