# Get a valid number from the user
def get_valid_number():
    user_input = float(input("Give a number between 50 and 100"))
    while user_input < 50 or user_input > 100:
        user_input = float(input("Give a number between 50 and 100"))
    return user_input


# Get ten valid numbers from the user
def get_ten_numbers():
    numbers_array = [0.0]*10
    for counter in range(0, len(numbers_array)):
        numbers_array[counter] = get_valid_number()
    return numbers_array


# Calculate average
def calc_average(numbers):
    total = 0
    for counter in range(0, len(numbers)):
        total += numbers[counter]
    average = total/len(numbers)
    return average


# Main Program
if __name__ == "__main__":
    number_array = get_ten_numbers()
    number_average = calc_average(number_array)
    print("The average of the numbers entered is:", round(number_average, 2))

