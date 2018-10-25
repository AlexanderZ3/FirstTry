def reverse(x):

    rev = 0
    while x!=0:
        last = x % 10
        x /= 10
        rev = rev*10 +last
    if rev>=(2**31) or rev<-(2**31):
        rev = 0
    return rev

print("enter an int num:")
x = int(input('>>>'))
print(reverse(x))
# 为什么输出老是0
