def primenum(x):
    if x <= 1:  # Numbers less than or equal to 1 are not prime
        return False
    for i in range(2, int(x**0.5) + 1):  # Check up to the square root of x
        if x % i == 0:  # If divisible, it's not prime
            return False
    return True  # If no divisors are found, it's prime
print(primenum(3))
x=int(input("Enter a number\n"))
print(primenum(x))
