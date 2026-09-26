# This is a program to check the GCD
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
print(gcd(48, 18))

def GCD(c,d):
    while d:
        c,d = d, c%d
    return a
print(GCD(12,6))
