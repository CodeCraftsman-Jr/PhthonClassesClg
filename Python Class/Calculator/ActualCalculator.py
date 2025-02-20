from addition import add
from subtraction import subtract
from multiplication import multiply
from division import divide
from modulus import modulus
from square import square

def main():
    print("Choose operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Square of a number")
    
    choice = input(" Choose any Operation from  (1-6): ")
    
    if choice == '6':
        num = float(input("Enter a number: "))
        print(f"Square of {num} is: {square(num)}")
    else:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print(f"The result is: {add(num1, num2)}")
        elif choice == '2':
            print(f"The result is: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"The result is: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"The result is: {divide(num1, num2)}")
        elif choice == '5':
            print(f"The result is: {modulus(num1, num2)}")
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()
