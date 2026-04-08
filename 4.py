# Task 3: Build a Contact Book
# Explanation:
# • Create a CLI-based contact book
# • Allow users to:
# o Add new contact

# o View all contacts
# o Search by name
# o Delete contact
# • Store contacts in a list of dictionaries
contacts = []

while True:
    print("\nContact Book Menu")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")

        contact = {"name": name, "phone": phone, "email": email}
        contacts.append(contact)

        print("Contact added successfully!")

    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts found.")
        else:
            print("\nAll Contacts:")
            for c in contacts:
                print("Name:", c["name"], "| Phone:", c["phone"], "| Email:", c["email"])

    elif choice == "3":
        search_name = input("Enter name to search: ")
        found = False

        for c in contacts:
            if c["name"].lower() == search_name.lower():
                print("Contact Found:")
                print("Name:", c["name"])
                print("Phone:", c["phone"])
                print("Email:", c["email"])
                found = True
                break

        if not found:
            print("Contact not found.")

    elif choice == "4":
        delete_name = input("Enter name to delete: ")
        found = False

        for c in contacts:
            if c["name"].lower() == delete_name.lower():
                contacts.remove(c)
                print("Contact deleted successfully!")
                found = True
                break

        if not found:
            print("Contact not found.")

    elif choice == "5":
        print("Exiting Contact Book...")
        break

    else:
        print("Invalid choice. Try again.")