expenses = []

def add_expense():
    name = input("Enter expense name: ")
    category = input("Enter category (Food, Travel, etc.): ")
    amount = float(input("Enter amount: "))
    expenses.append({"name": name, "category": category, "amount": amount})
    print(f"Added: {name}, {category}, ${amount}")

def show_expenses():
    if not expenses:
        print("No expenses yet!")
    else:
        print("Your expenses:")
        for i, e in enumerate(expenses, 1):
            print(f"{i}. {e['name']} - {e['category']} - ${e['amount']}")

def total_by_category():
    totals = {}
    for e in expenses:
        totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]
    for cat, amt in totals.items():
        print(f"{cat}: ${amt}")

while True:
    print("\n1. Add Expense  2. Show Expenses  3. Total by Category  4. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        total_by_category()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
