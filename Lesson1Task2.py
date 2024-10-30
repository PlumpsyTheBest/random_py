# Calculates the area of a rectangle.
def rectangle_area(width, height):
    return width*height


# Calculates the perimeter of a rectangle.
def rectangle_perimeter(width, height):
    return (width+height)*2


# Prompts the user for a valid rectangle dimension and returns it.
def get_valid_dimension(typeoflength):
    length = input("What is the " + typeoflength)
    while length <= 0:
        length = input("Wrong try again what is the " + typeoflength)
    return length


if __name__ == "__main__":
    rectangle_width = get_valid_dimension("width")
    rectangle_height = get_valid_dimension("height")
    area = rectangle_area(rectangle_width, rectangle_height)
    perimeter = rectangle_perimeter(rectangle_width, rectangle_height)
    print("Area:", area)
    print("Perimeter:", perimeter)
