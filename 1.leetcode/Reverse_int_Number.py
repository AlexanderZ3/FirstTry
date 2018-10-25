def reverse(x):
        """
        :type x: int
        :rtype: int
        """
    rev = 0
    while(x!= 0):
        last = x %10
        x /= 10
        rev = rev *10 + pop

    if rev>=(2**31) or rev <-(2**31):
        rev = 0
    return rev

print("please enter a int number:")
x = int(input())
print(reverse(x))
