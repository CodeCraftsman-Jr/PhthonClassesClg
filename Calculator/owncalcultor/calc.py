from modules import add
from modules import subtract
from modules import multiply
from modules import divide
from modules import modulus
from modules import square

while True:
    # Prompt the user for operation choice
    n = int(input("Enter a number from 1 to 6 \n1: Add \n 2: Subtract\n 3: Multiply\n 4: Divide\n 5: Modulus\n 6: Square\n 0: Exit "))

    if n == 0:
        print("Exiting the program. Goodbye!")
        break  # Exit the loop if user chooses to exit

    if n == 6:
        g = int(input("Enter a number to square: "))
        print(f"The square of {g} is {square(g)}")
    else:
        y = int(input("Enter the first number: "))
        z = int(input("Enter the second number: "))
        
        if n == 1:
            print(f"The sum is: {add(y, z)}")
        elif n == 2:
            print(f"The difference is: {subtract(y, z)}")
        elif n == 3:
            print(f"The product is: {multiply(y, z)}")
        elif n == 4:
            print(f"The quotient is: {divide(y, z)}")
        elif n == 5:
            print(f"The modulus is: {modulus(y, z)}")
        else:
            print("Invalid option. Please choose a valid number from 1 to 6.")

    
    cont = input("Do you want to perform another operation? (yes/no): ").lower()
    if cont != 'yes':
        print("Exiting the program. Goodbye!")
        break 
