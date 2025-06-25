#Date created: 4/9/2025
#Creator: Abimael Royer (solarus)

from expense import Expense
import calendar
import datetime

def main():
    print("Welcome to sol's data expense app! ٩(ˊᗜˋ )و \n") 
    expenseFilePath = "expenses.csv"
    budget = 2000

#  IMPORTANT: Comment out get_expense and save_expense if you don't want to add a new expense

#   1. user input for expense
    #expense = get_expense()
#   2. write expense to file
    #save_expense(expense, expenseFilePath)
#   3. read file, sum up expenses
    sum_expense(expenseFilePath, budget)
    


def get_expense():
    # receives expense name and amount
    print("getting user expense")
    expenseName = input("enter expense name: ")
    expenseAmount = float(input("enter the cost: "))

    # creates list of acceptable categories
    expenseCategories = [
        "[!] Food", 
        "[!] Home", 
        "[!] Work", 
        "[!] Fun", 
        "[!] Misc"
    ]

    # prompts user to choose a category by picking a number between 1-5. Invalid choice will prompt user to try again
    while True:
        print("Select a category")
        for i, categoryName in enumerate(expenseCategories):
            print(f" {i+1}. {categoryName}")

        choiceRange = f"[1 - {len(expenseCategories)}]"
        categoryChoice = int(input(f"Enter a number {choiceRange}: ")) -1

        if categoryChoice in range(len(expenseCategories)):
            selectedCategory = expenseCategories[categoryChoice]
            newExpense = Expense(name = expenseName, category = selectedCategory, amount = expenseAmount )
            return newExpense
        else:
            print("Invalid. Please try again!")

def save_expense(expense: Expense, expenseFilePath):
    #takes user expense and saves it to a csv file
    print(f"saving user expense: {expense} to {expenseFilePath}")
    with open(expenseFilePath, "a") as f:
        f.write(f"{expense.name},{expense.category},{expense.amount}\n")



def sum_expense(expenseFilePath, budget):
    print("summing up user expense")
    #creates an expense list using csv file
    expenses: list[Expense] = []
    with open(expenseFilePath, "r") as f:
        lines = f.readlines()
        for line in lines:
            expenseName, expenseCategory, expenseAmount = line.strip().split(",")
            lineExpense = Expense(name = expenseName, category = expenseCategory, amount = float(expenseAmount))
            expenses.append(lineExpense)

    # adds up all the expenses and gives you the total by category
    amountByCategory = {}
    for expense in expenses:
        key = expense.category
        if key in amountByCategory:
            amountByCategory[key] += expense.amount
        else:
            amountByCategory[key] = expense.amount

    #prints out the total expenses by category
    print ("Expenses By Category:")
    for key, amount in amountByCategory.items():
        print(f"  {key}: ${amount:.2f}")

    #prints out total expense amount
    totalSpent = sum([x.amount for x in expenses])
    print(f"Total spent ${totalSpent:.2f} this month!")

    #calculates money leftover after expenses
    remainingBudget = budget - totalSpent
    print(f"Budget Remaining: ${remainingBudget:.2f}")


    now = datetime.datetime.now()
    daysInMonth = calendar.monthrange(now.year, now.month)[1]
    remainingDays = daysInMonth - now.day

    #using the calendar and datetime library, calculate remaining budget for each day, depending on how many days are left in the month
    dailyBudget = remainingBudget / remainingDays
    # this function frints out the daily budget in green text
    print(green(f"Budget Per Day: ${dailyBudget:.2f}"))

#colored text function (aesthetic)
def green(text):
    return f"\033[92m{text}\033[0m"

if __name__== "__main__":
    main()