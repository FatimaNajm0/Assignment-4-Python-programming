import Q8_sorting

while True:
    print("\n--- Sorting Menu ---")
    print("1. Bubble Sort")
    print("2. Merge Sort")
    print("3. Quick Sort")
    print("4. Exit")
    
    choice = input("Choose an option: ")
    
    if choice in ['1', '2', '3']:
        user_input = input("Enter numbers separated by spaces: ")
        my_list = []
        for x in user_input.split():
            my_list.append(int(x))
            
        if choice == '1':
            print("Sorted List:", sorting.bubble_sort(my_list))
        elif choice == '2':
            print("Sorted List:", sorting.merge_sort(my_list))
        elif choice == '3':
            print("Sorted List:", sorting.quick_sort(my_list))
            
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice, try again.")
