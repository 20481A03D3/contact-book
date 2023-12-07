class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number, email, address):
        self.contacts[name] = {
            'phone_number': phone_number,
            'email': email,
            'address': address
        }
        print(f"Contact '{name}' added successfully!")

    def view_contact_list(self):
        if not self.contacts:
            print("Contact list is empty.")
        else:
            print("\nContact List:")
            for name, details in self.contacts.items():
                print(f"{name}: {details['phone_number']}")

    def search_contact(self, keyword):
        results = []
        for name, details in self.contacts.items():
            if keyword.lower() in name.lower() or keyword in details['phone_number']:
                results.append((name, details))
        return results

    def update_contact(self, name, new_phone_number, new_email, new_address):
        if name in self.contacts:
            self.contacts[name]['phone_number'] = new_phone_number
            self.contacts[name]['email'] = new_email
            self.contacts[name]['address'] = new_address
            print(f"Contact '{name}' updated successfully!")
        else:
            print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully!")
        else:
            print(f"Contact '{name}' not found.")


def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email address: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone_number, email, address)

        elif choice == '2':
            contact_book.view_contact_list()

        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            results = contact_book.search_contact(keyword)
            if results:
                print("\nSearch Results:")
                for name, details in results:
                    print(f"{name}: {details['phone_number']}")
            else:
                print("No matching contacts found.")

        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            new_phone_number = input("Enter new phone number: ")
            new_email = input("Enter new email address: ")
            new_address = input("Enter new address: ")
            contact_book.update_contact(name, new_phone_number, new_email, new_address)

        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)

        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
