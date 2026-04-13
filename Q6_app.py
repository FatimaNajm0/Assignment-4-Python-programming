import Q6_simple_math

while True:
    print("\n--- Math App ---")
    print("1. Calculate Factorial")
    print("2. Check Prime")
    print("3. Check Positive or Negative")
    print("4. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == '1':
        num = int(input("Enter a number: "))
        print(f"Factorial: {simple_math.factorial(num)}")
        
    elif choice == '2':
        num = int(input("Enter a number: "))
        print(f"Is prime? {simple_math.is_prime(num)}")
        
    elif choice == '3':
        num = int(input("Enter a number: "))
        print(f"Sign: {simple_math.check_sign(num)}")
        
    elif choice == '4':
        print("Exiting...")
        break
        
    else:
        print("Invalid choice!")
