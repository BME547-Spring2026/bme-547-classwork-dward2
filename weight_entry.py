def input_weight_entry():
    print("Enter patient weight in form of ## units (e.g., 105 lb)")
    weight_input = input("Enter weight: ")
    weight_in_kg = parse_weight_input(weight_input)
    print("The patient weight of {} kg will be stored "
          "in database.".format(weight_in_kg))


def parse_weight_input(weight_input):
    try:
        weight, units = weight_input.split(' ')
    except ValueError:
        return -99
    weight = float(weight)
    units = units.lower()
    if units in ["lb", "lbs", "pound", "pounds"]:
        weight_kg = convert_lb_to_kg(weight)
    elif units in ["kg", "kgs", "kilograms", "kilograms"]:
        weight_kg = weight
    weight_kg = round(weight_kg)
    if weight_kg > 1000:
        return -99
    return weight_kg


def convert_lb_to_kg(weight_lb):
    weight_kg = weight_lb / 2.20462
    return weight_kg


if __name__ == "__main__":
    input_weight_entry()
