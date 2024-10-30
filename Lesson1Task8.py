# Get valid item cost
def get_valid_item_cost():
    item_cost = float(input("What is the item cost"))
    while float(item_cost) <= 0:
        item_cost = float(input("What is the item cost"))
    return item_cost


# Get item costs from the user in an array
def get_multiple_item_costs():
    item_cost_array = []
    more_items = ""
    item_value = 0
    while more_items != "no":
        item_value = get_valid_item_cost()
        item_cost_array.append(item_value)
        more_items = input("Do you want to get another item")
    return item_cost_array


# Calculate the subtotal
def calculate_subtotal(prices):
    total = 0.0
    for i in range(0, len(prices)):
        total = total + prices[i]
    return total


# Calculate VAT and add to subtotal
def calculate_total_with_vat(subtotal):
    return subtotal*1.2


# Main program
if __name__ == "__main__":
    items_cost = get_multiple_item_costs()
    sub_total = calculate_subtotal(items_cost)
    calculate_total_with_vat(sub_total)
