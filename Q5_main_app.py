import Q5_edit_list

my_list = []

while True:
    print("\n--- Menu ---")
    print("1. Add element")
    print("2. Delete element")
    print("3. Update element")
    print("4. Show list")
    print("5. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == '1':
        elem = input("Enter element to add: ")
        edit_list.add_element(my_list, elem)
        
    elif choice == '2':
        elem = input("Enter element to delete: ")
        edit_list.delete_element(my_list, elem)
        
    elif choice == '3':
        old_val = input("Enter element to update: ")
        new_val = input("Enter new element: ")
        edit_list.update_element(my_list, old_val, new_val)
        
    elif choice == '4':
        print(f"Current List: {my_list}")
        
    elif choice == '5':
        print("Exiting application...")
        break
        
    else:
        print("Invalid choice, please try again.")
