def main():
    shopping_list = []

    while True:
        print("\nMenu:")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View List")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()
        print(f"DEBUG: You entered -> '{choice}'")  # Debugging

        if choice == '1':
            item = input("Enter item: ").strip()
            shopping_list.append(item)
            print(f"Added {item}")

        elif choice == '2':
            if not shopping_list:
                print("List empty")
            else:
                item = input("Enter item to remove: ").strip()
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"Removed {item}")
                else:
                    print("Not found")

        elif choice == '3':
            print("Shopping List:", shopping_list if shopping_list else "Empty")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
