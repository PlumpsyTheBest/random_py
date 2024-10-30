# Get an array of hours for each day of the week
def get_hours():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    hour_array = [0]*len(days)
    for counter in range(len(days)):
        user_input = int(input("How many hours did you work on " + days[counter]))
        hour_array[counter] = validate_hours(user_input)
    return hour_array


# Validates hours input ensuring between 1 and 24.

def validate_hours(user_input):
    while user_input < 1 or user_input > 24:
        user_input = int(input("Wrong answer please enter again"))
    return user_input


# Calculates total hours.
def track_hours(hours_array):
    total = 0
    for counter in range(len(hours_array)):
        total += hours_array[counter]
    return total


# Calculate pay for this week including overtime
def calculate_pay(hours_worked, pay):
    if hours_worked > 35:
        total = (35*pay) + (1.5*pay*(hours_worked-35))
    else:
        total = hours_worked*pay
    return total


# Get a valid hourly pay from the user
def get_hourly_pay():
    user_input = float(input("What is the hourly pay"))
    while user_input < 11.44 or user_input > 15:
        user_input = float(input("Wrong enter pay again"))
    return user_input


# Main Program
if __name__ == "__main__":
    hours_worked = get_hours()
    total_hours_worked = track_hours(hours_worked)
    hourly_pay = get_hourly_pay()
    pay_for_week = calculate_pay(total_hours_worked, hourly_pay)
