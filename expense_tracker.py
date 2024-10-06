from expense import Expense
def main():
    print(f"🎯 Running expense Tracker")
    expense_file_name = "expenses.csv"
    

    #GET USER INPUT for expense.
    expense = get_user_expense()
    #write their expense to a file
    save_expense_to_file(expense, expense_file_name)


    #read file and sumarize expenses
    summarize_expense(expense_file_name)

def get_user_expense():
    print(f"🎯 Getting user expense")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    print(f"you have entered an expense: {expense_name}, {expense_amount} ")


    expense_categories = [
        "🍔 Food", "🏠 home", "✈️ travel", "👕 clothing", "🛝 fun"
    ]

    while True:
        print("Select the category items:")
        for i, expense_category in enumerate(expense_categories):
            print(f"{i+1} : {expense_category}")
        

        value_range = f"[1- {len(expense_category)}]"
        selected_index = int(input(f"Select an expense category {value_range}: "))

        if selected_index > 0 and selected_index <= len(expense_category):
            new_expense = Expense(expense_name,expense_amount, expense_categories[selected_index-1])
            return new_expense
        else:
            print("Invalid input. Please try again.")
        break
    


def save_expense_to_file(expense: Expense, expense_file_name):

    print(f"🎯 Saving {expense} to {expense_file_name}")
    with open(expense_file_name, "a", encoding="utf-8") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")

def summarize_expense(expense_file_name):
    print(f"🎯 Summarizing user expense")
    expenses = []
    with open(expense_file_name, "r",encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, eexpense_amount, expense_category = line.strip().split(",")
            print(expense_name, eexpense_amount, expense_category)

   




if __name__ == "__main__":
    main()