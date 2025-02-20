num = int(input("Enter a number: "))

# Loop through numbers from 2 to num-1
for i in range(2, num):
    is_prime = True  # Assume the number is prime initially

    # Check if i is divisible by any number between 2 and sqrt(i)
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break  # No need to check further if i is divisible by j

    if is_prime:
        print(i)
