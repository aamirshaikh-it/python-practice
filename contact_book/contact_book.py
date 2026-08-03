class contact:
    def __init__(self, name, number, email):
        self.name = name
        self.number = number
        self.email = email

contacts = []
while True:
    userinput = input("Would you like to View, Add, Delete a contact, or Quit? (v/a/d/q): ").lower()
    if userinput == "view" or userinput == "v":
        for c in contacts:
            print("-" * 20)
            print(f"Name: {c.name}")
            print(f"Number: {c.number}")
            print(f"Email: {c.email}")
            print("-" * 20)
    elif userinput == "add" or userinput == "a":
        nameinput = input("Enter the contact's name: ")
        numberinput = input("Enter the contact's phone number: ")
        emailinput = input("Enter the contact's email: ")
        new_contact = contact(nameinput, numberinput, emailinput)
        contacts.append(new_contact)
        print("Contact added successfully.")
    elif userinput == "delete" or userinput == "d":
        delete_contact = input("Enter the name of the contact you want to delete: ")
        found = False
        for c in contacts:
            if c.name == delete_contact:
                contacts.remove(c)
                found = True
                break
        if not found:
            print("No contact found with that name.")
        else:
            print("Contact deleted successfully.")
    elif userinput == "quit" or userinput == "q":
        print("Goodbye!")
        break
    else:
        print("Invalid input. Please type view, add, delete, or quit.")