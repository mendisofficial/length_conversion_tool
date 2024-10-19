def metric_to_imperial(value, from_unit, to_unit):
    conversion_factors = {
        ('mm', 'in'): 0.0393701,
        ('cm', 'in'): 0.393701,
        ('m', 'in'): 39.3701,
        ('km', 'in'): 39370.1,
        ('mm', 'ft'): 0.00328084,
        ('cm', 'ft'): 0.0328084,
        ('m', 'ft'): 3.28084,
        ('km', 'ft'): 3280.84,
        ('mm', 'yd'): 0.00109361,
        ('cm', 'yd'): 0.0109361,
        ('m', 'yd'): 1.09361,
        ('km', 'yd'): 1093.61,
        ('mm', 'mi'): 6.2137e-7,
        ('cm', 'mi'): 6.2137e-6,
        ('m', 'mi'): 0.000621371,
        ('km', 'mi'): 0.621371
    }
    return value * conversion_factors[(from_unit, to_unit)]


def imperial_to_metric(value, from_unit, to_unit):
    conversion_factors = {
        ('in', 'mm'): 25.4,
        ('in', 'cm'): 2.54,
        ('in', 'm'): 0.0254,
        ('in', 'km'): 2.54e-5,
        ('ft', 'mm'): 304.8,
        ('ft', 'cm'): 30.48,
        ('ft', 'm'): 0.3048,
        ('ft', 'km'): 0.0003048,
        ('yd', 'mm'): 914.4,
        ('yd', 'cm'): 91.44,
        ('yd', 'm'): 0.9144,
        ('yd', 'km'): 0.0009144,
        ('mi', 'mm'): 1.609e+6,
        ('mi', 'cm'): 160934,
        ('mi', 'm'): 1609.34,
        ('mi', 'km'): 1.60934
    }
    return value * conversion_factors[(from_unit, to_unit)]


def main():
    print("Welcome to the Length Conversion Tool!\n")
    print("Please select a conversion type:")
    print("1. Metric to Imperial")
    print("2. Imperial to Metric")
    conversion_type_choice = int(input("Enter your choice (1 or 2): "))

    match conversion_type_choice:
        case 1:
            print("\nSelect the unit to convert from:")
            print("1. mm")
            print("2. cm")
            print("3. m")
            print("4. km")
            from_unit_choice = int(input("Enter your choice (1-4): "))
            metric_units = ['mm', 'cm', 'm', 'km']
            from_unit = metric_units[from_unit_choice - 1]

            print("\nSelect the unit to convert to:")
            print("1. in")
            print("2. ft")
            print("3. yd")
            print("4. mi")
            to_unit_choice = int(input("Enter your choice (1-4): "))
            imperial_units = ['in', 'ft', 'yd', 'mi']
            to_unit = imperial_units[to_unit_choice - 1]

            value = float(input(f"\nEnter the value in {from_unit}: "))
            result = metric_to_imperial(value, from_unit, to_unit)
            print(f"\n{value} {from_unit} is equal to {result:.2f} {to_unit}.")

        case 2:
            print("\nSelect the unit to convert from:")
            print("1. in")
            print("2. ft")
            print("3. yd")
            print("4. mi")
            from_unit_choice = int(input("Enter your choice (1-4): "))
            imperial_units = ['in', 'ft', 'yd', 'mi']
            from_unit = imperial_units[from_unit_choice - 1]

            print("\nSelect the unit to convert to:")
            print("1. mm")
            print("2. cm")
            print("3. m")
            print("4. km")
            to_unit_choice = int(input("Enter your choice (1-4): "))
            metric_units = ['mm', 'cm', 'm', 'km']
            to_unit = metric_units[to_unit_choice - 1]

            value = float(input(f"\nEnter the value in {from_unit}: "))
            result = imperial_to_metric(value, from_unit, to_unit)
            print(f"\n{value} {from_unit} is equal to {result:.2f} {to_unit}.")

        case _:
            print("Invalid choice")


if __name__ == "__main__":
    main()
