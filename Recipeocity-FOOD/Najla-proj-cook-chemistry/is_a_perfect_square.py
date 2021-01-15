from math import sqrt
def is_square(a):
    answer = ""
    root = sqrt(a)
    if (int(root + 0.5))**2 == a:
        answer = "is a perfect square"
    else:
        answer = "is not a perfect square"
    return answer

a = 25
print(is_square(16) )

