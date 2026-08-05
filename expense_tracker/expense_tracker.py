while True:

    userinput = input("Add / View / Total / Quit: ").lower() 

    if userinput == "add":
        amountinput = input("Enter the amount: ")
        categoryinput = input("Enter the category: ")
        descriptioninput = input("Enter a description: ")
        with open("expense.txt" , "a") as f:
            f.write(f"{amountinput},{categoryinput},{descriptioninput}\n")
        print("Expense added successfully")
    elif userinput == "view":
        try:
            with open("expense.txt", "r") as f:
                expense = f.readlines()
            for i in expense:
                print(i.strip())
        except FileNotFoundError:
            print("There Is No Expense Added Yet!")
    elif userinput == "total":
        try:
            with open("expense.txt", "r") as f:
                expense = f.readlines()

            total = 0
            for i in expense:
                parts = i.split(",")
                amount = parts[0]
                total += int(amount)
            print(total)
        except FileNotFoundError:
            print("No Expense Recorded Yet. Your Total: 0")

    elif userinput == "quit" or userinput == "q" :
        break

    else:
        print("Invalid input. Please Choose Form Add / View / Total / Quit.")