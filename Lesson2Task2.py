# Parses the invoice string to convert it to an array of float prices.
def parse_invoice(input):
    temp_array = input.split(";")
    output_array = [0.0] * len(temp_array)
    for i in range(0, len(temp_array)):
        output_array[i] = float(temp_array[i])
    return output_array


# Calculates the total price from the invoice
def calc_total(array_of_prices):
    total = 0
    for i in range(0, len(array_of_prices)):
        total = total + float(array_of_prices[i])
    return total


# Applies a discount to the total amount if it exceeds a threshold.
def apply_discount(total, threshold, discount):
    if total > threshold:
        total = total - (total * (discount/100))
    return total


# Main Program
if __name__ == "__main__":

    #INPUTS

    invoice_input = input("Enter item prices separated by commas: ")
    threshold_input = float(input("Enter discount threshold: "))
    discount_percentage_input = float(input("Enter discount percentage: "))

    #CALCULATIONS

    prices_array = parse_invoice(invoice_input)
    invoice_total = calc_total(prices_array)
    invoice_discounted_amount = apply_discount(invoice_total, threshold_input, discount_percentage_input)

    #OUTPUTS

    print("Total amount before discount: £" + str(round(invoice_total, 2)))
    print("Total amount after discount: £" + str(round(invoice_discounted_amount, 2)))
