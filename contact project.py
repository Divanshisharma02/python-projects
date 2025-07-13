# File-Based Contact Book - Mini Project 

# Function to add a new contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")

    # Open the file in append mode and write contact details
    with open("contacts.txt", "a") as f:
        f.write(name + "," + phone + "," + email + "\n")

    print("Contact added successfully.")

# Function to view all saved contacts
def view_contacts():
    try:
        # Open the file in read mode
        with open("contacts.txt", "r") as f:
            lines = f.readlines()

            if not lines:
                print("No contacts found.")
            else:
                print("All Contacts:")
                for line in lines:
                    # Separate name, phone, and email from the line
                    name, phone, email = line.strip().split(",")
                    print("Name:", name, "| Phone:", phone, "| Email:", email)
    except FileNotFoundError:
        print("Contact file not found.")

# Function to search for a contact by name
def search_contact():
    search_name = input("Enter name to search: ")
    found = False

    try:
        with open("contacts.txt", "r") as f:
            for line in f:
                name, phone, email = line.strip().split(",")

                # Check if the search term is in the name
                if search_name.lower() in name.lower():
                    print("Name:", name, "| Phone:", phone, "| Email:", email)
                    found = True

        if not found:
            print("Contact not found.")
    except FileNotFoundError:
        print("Contact file not found.")

# Function to update contact details
def update_contact():
    name_to_update = input("Enter the name of the contact to update: ")
    updated = False

    try:
        # Read all contacts into a list
        with open("contacts.txt", "r") as f:
            lines = f.readlines()

        # Rewrite the file with updated content
        with open("contacts.txt", "w") as f:
            for line in lines:
                name, phone, email = line.strip().split(",")

                if name.lower() == name_to_update.lower():
                    # Ask for new details
                    new_name = input("Enter new name: ")
                    new_phone = input("Enter new phone: ")
                    new_email = input("Enter new email: ")

                    # Write the updated contact
                    f.write(new_name + "," + new_phone + "," + new_email + "\n")
                    updated = True
                else:
                    # Write the old contact back
                    f.write(line)

        if updated:
            print("Contact updated successfully.")
        else:
            print("Contact not found.")
    except FileNotFoundError:
        print("Contact file not found.")

# Function to delete a contact
def delete_contact():
    name_to_delete = input("Enter the name of the contact to delete: ")
    deleted = False

    try:
        with open("contacts.txt", "r") as f:
            lines = f.readlines()

        # Rewrite the file excluding the deleted contact
        with open("contacts.txt", "w") as f:
            for line in lines:
                name, phone, email = line.strip().split(",")

                if name.lower() != name_to_delete.lower():
                    f.write(line)
                else:
                    deleted = True

        if deleted:
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")
    except FileNotFoundError:
        print("Contact file not found.")

# Main menu to show options repeatedly
def main():
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        # Take user's choice
        choice = input("Enter your choice: ")

        # Call respective function based on choice
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Program starts here
if __name__ == "__main__":
    main()








