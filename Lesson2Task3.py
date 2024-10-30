# Calculates the number of buses needed given a bus capacity.
def calculate_buses_needed(people):
    busses_required = people / 45
    if people % 45 > 0:
        busses_required += 1
    busses_required = int(busses_required)
    return busses_required


# Calculate cost per person
def cost_per_person(people, bus_amount):
    cost = (bus_amount*125)/people
    cost = round(cost, 2)
    return cost


# Main Program
if __name__ == "__main__":
    people_amount = int(input("How many people"))
    busses_needed = calculate_buses_needed(people_amount)
    cost_per_persons = cost_per_person(people_amount, busses_needed)