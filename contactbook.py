
#Contact Book using Dictionary

contacts = {}

def add_contact():
    name = input("Enter contact name: ").strip()
    if name in contacts:
        print(f"Contact '{name}' already exists! Use update instead.")
        return
    phone = input("Enter phone number: ").strip()
    contacts[name] = phone
    print(f"Contact '{name}' added successfully!")


def search_contact():
    name = input("Enter name to search: ").strip()
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print(f"Contact '{name}' not found.")


def update_contact():
    name = input("Enter name to update: ").strip()
    if name in contacts:
        new_phone = input("Enter new phone number: ").strip()
        contacts[name] = new_phone
        print(f"Contact '{name}' updated successfully!")
    else:
        print(f"Contact '{name}' not found.")


def delete_contact():
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print(f"Contact '{name}' not found.")


def show_all_contacts():
    if not contacts:
        print("No contacts saved yet.")
        return
    print("\n--- All Contacts ---")
    for name, phone in contacts.items():
        print(f"{name}: {phone}")
    print("---------------------")


def show_menu():
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Show All Contacts")
    print("6. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            show_all_contacts()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1-6.")

if __name__ == "__main__":
    main()