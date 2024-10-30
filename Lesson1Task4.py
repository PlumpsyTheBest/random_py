# Validates input of expense to ensure positive number.
def validate_expense(user_input):
    while user_input < 0:
        user_input = float(input("Incorrect please input again"))
    return user_input


# Calculates total expenses.
def calculate_total_expenses(expenses):
    total = 0
    for counter in range(len(expenses)):
        total += expenses[counter]
    return total


# Get an array of expenses for each category.
def get_expenses():
    category = [
        "housing", "transport", "shopping", "utilities",
        "insurance", "debt", "entertainment", "other"]
    expenses = [0.0] * len(category)
    for counter in range(0, len(category)):
        user_input = float(input("What is the price for " + str(category[counter])))
        expenses[counter] = validate_expense(user_input)
    return expenses


# Calculate remaining budget
def calculate_remaining_budget(total_expenses, budget):
    return budget - total_expenses


# Display the months total expenses and the remaining budget
def display_expenses_and_remaining_budget(total_expenses, budget):
    print("Total expense is " + str(total_expenses))
    print("Your budget is " + str(budget))


# Main Program
if __name__ == "__main__":
    budget = float(input("What is your budget"))

    expenses = get_expenses()
    total_expenses = calculate_total_expenses(expenses)
    budget = calculate_remaining_budget(total_expenses, budget)
    display_expenses_and_remaining_budget(total_expenses, budget)
