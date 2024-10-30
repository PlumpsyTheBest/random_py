from random import randint


# Generate an array for 6 random numbers between 1 and 60
def generate_random_numbers():
    random_number_array = [0] * 6
    for i in range(0, len(random_number_array)):
        random_number_array[i] = randint(1, 60)
    return random_number_array


# Display any number from the array that is over 20
def display_over_20(numbers):
    for i in range(0, len(numbers)):
        if numbers[i] > 20:
            print(numbers[i])


# Main program
if __name__ == '__main__':
    array_of_random_numbers = generate_random_numbers()
    display_over_20(array_of_random_numbers)
