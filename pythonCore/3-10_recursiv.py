n = 2
k = 1


def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n-1)
 

def number_of_groups(n, k):
    return int(factorial(n) / (factorial(n-k) * factorial(k)))

print(factorial(n) / (factorial(n-k) * factorial(k)))