def sum1(num):
    num = num.split()
    num = map(int, num)
    num = sum(num)
    return num


nums = input("Enter the Numbers:\n")
print(sum1(nums))


# another way

# def sm():
#     nums = input("Enter the Numbers:")
#     cs = list(map(int, nums.split()))
#     # print(sum(cs))
#     return sum(cs)

# print(sm())




