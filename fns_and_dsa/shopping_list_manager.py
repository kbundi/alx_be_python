shopping_list = []

def add_item():
    item = input("Enter the item to add: ").strip()
    if item:
        shopping_list.append(item)
        print(f"'{item}' added to the shopping list.")
    else:
        print("Item name cannot be empty.")

def remove_item():
    item = input("Enter the item to remove: ").strip()
    if item:
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' removed from the shopping list.")
        else:
            print(f"'{item}' not found in the shopping list.")
    else:
        print("Item name cannot be empty.")

def view_list():
    if shopping_list:
        print("\nCurrent Shopping List:")
        for index, item in enumerate(shopping_list):
            print(f"{index + 1}. {item}")
    else:
        print("The shopping list is empty.")

def main():
    while True:
        print("\nShopping List Manager")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View List")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            add_item()
        elif choice == '2':
            remove_item()
        elif choice == '3':
            view_list()
        elif choice == '4':
            print("Exiting the shopping list manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
