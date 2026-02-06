import os

FILE_NAME = "finance_data.txt"

def add_entry():
    entry_type = input("Enter type (income/expense): ").strip().lower()
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    with open(FILE_NAME, "a") as f:
        f.write(f"{entry_type},{amount},{description}\n")
    print("Entry added successfully!\n")

def show_summary():
    total_income = 0
    total_expense = 0

    if not os.path.exists(FILE_NAME):
        print("No data found. Please add entries first.\n")
        return

    with open(FILE_NAME, "r") as f:
        for line in f:
            entry_type, amount, description = line.strip().split(",")
            amount = float(amount)
            if entry_type == "income":
                total_income += amount
            elif entry_type == "expense":
                total_expense += amount

    balance = total_income - total_expense
    print("\n--- Summary ---")
    print(f"Total Income: {total_income}")
    print(f"Total Expenses: {total_expense}")
    print(f"Balance: {balance}\n")

def main():
    while True:
        print("1. Add Entry")
        print("2. Show Summary")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_entry()
        elif choice == "2":
            show_summary()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
