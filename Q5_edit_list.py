def add_element(lst, element):
    lst.append(element)
    print("Element added successfully!")

def delete_element(lst, element):
    if element in lst:
        lst.remove(element)
        print("Element deleted successfully!")
    else:
        print("Element not found!")

def update_element(lst, old_element, new_element):
    if old_element in lst:
        index = lst.index(old_element)
        lst[index] = new_element
        print("Element updated successfully!")
    else:
        print("Element not found!")
