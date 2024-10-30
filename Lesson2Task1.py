# Prompts the user to enter a positive integer for the number of apples.
def get_number_apples():
    apple_amount = int(input("How many apples do you have "))
    while apple_amount <= 0:
        apple_amount = int(input("How many apples do you have "))
    return apple_amount

# Calculates and returns the number of leftover apples.
def calc_leftover_apples(apples):
    leftover = apples % 20
    return leftover

# Calculates how many apples each pupil should be given.
def calc_apple_per_pupil(apples):
    pupil_apple_amount = int(apples/20)
    return pupil_apple_amount

# Main Program
if __name__ == "__main__":
    number_apples = get_number_apples()
    leftover_apples = calc_leftover_apples(number_apples)
    apple_per_pupil = calc_apple_per_pupil(number_apples)


