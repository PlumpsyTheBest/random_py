# Calculates simple interest based on principal, rate, and time.
def calculate_simple_interest(principal, rate, time):
    return (principal*rate*time)/100


if __name__ == "__main__":

    principal = float(input("What is the principal amount"))
    rate = float(input("What is the annual interest rate"))
    time = float(input("What is the time in years"))

    interest = calculate_simple_interest(principal, rate, time)
    print("Simple Interest:", interest)
