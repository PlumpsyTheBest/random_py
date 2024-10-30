# Get employee names and performance scores
def get_employee_data(amount):
    name_array = [""]*amount
    score_array = [0]*amount
    for counter in range(0, amount):
        name_array[counter] = input("What is the name of employee " + str(counter + 1))
        score_array[counter] = get_valid_score()
    return name_array, score_array


# Get a valid score from the user
def get_valid_score():
    score = -1
    while score < 0 or score > 100:
        score = float(input("What is the score for this employee"))
    return score


# Calculate average performance score, rounded to 0 dp
def calculate_average(scores):
    total = 0
    for counter in range(len(scores)):
        total = total + scores[counter]
    average = round((total/len(scores)), 0)
    return average


# Find the employees who are above the average and return an array of those employees names
def find_above_average_employees(names, scores, average):
    above_average = []
    for counter in range(len(names)):
        if scores[counter] > average:
            above_average.append(names[counter])
    return above_average


# Display the average performance score and the employees who are above average
def display_results(avg_score, above_avg_employee):
    print("The average score is : " + str(avg_score))
    for counter in range(len(above_avg_employee)):
        print(above_avg_employee[counter])


# Main Program
if __name__ == "__main__":
    employee_number = int(input("Enter the number of employees: "))
    employee_names, employee_scores = get_employee_data(employee_number)
    average_score = calculate_average(employee_scores)
    above_average_employees = find_above_average_employees(employee_names, employee_scores, average_score)
    display_results(average_score, above_average_employees)
