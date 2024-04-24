#  gcd табу : 1 нұсқа

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


number1 = 64
number2 = 72
print("Екі санның ЕҮОБ:", gcd(number1, number2))


#  gcd табу : 2 нұсқа

def euclidean_gcd(a, b):
    if b == 0:
        return a
    else:
        return euclidean_gcd(b, a % b)


number_1 = 37
number_2 = 185
print("Екі санның ЕҮОБ:", gcd(number_1, number_2))
