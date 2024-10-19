print("Welcome to the Length Conversion Tool!")
print("""Please select a conversion type:

1. Metric to Imperial
2. Imperial to Metric 

Enter your choice (1 or 2):""")

choice = int(input(">>>"))

match choice:
    case 1:
        print("""
    Select the unit to convert from:


    1. cm
    2. m

    Enter your choice (1 or 2):
    """)
        from_unit = int(input(">>>"))

        print("""
    Select the unit to convert to:

    1. inch
    2. feet

    Enter your choice (1 or 2):
    """)
        to_unit = int(input(">>>"))

        if from_unit == 1:
            if to_unit == 1:
                cm = float(input("Enter the centimeters : "))
                inch = cm * 0.3937
                print(f"{cm} cm is equal to {inch} inch")
            elif to_unit == 2:
                cm = float(input("Enter the centimeters : "))
                feet = cm * 0.0328
                print(f"{cm} cm is equal to {feet} feet")
            else:
                print("Invalid choice")
        elif from_unit == 2:
            if to_unit == 1:
                m = float(input("Enter in meters : "))
                inch = m * 39.37
                print(f"{m} m is equal to {inch} inch")
            elif to_unit == 2:
                m = float(input("Enter in meters : "))
                feet = m * 3.28
                print(f"{m} m is equal to {feet} feet")
            else:
                print("Invalid choice")
    case 2:
        print("""Select the unit to convert from:

    1. in
    2. ft

    Enter your choice (1 or 2): """)
        from_unit = int(input(">>>"))

        print("""Select the unit to convert to:

    1. cm
    2. m

    Enter your choice (1 or 2): """)
        to_unit = int(input(">>>"))

        if from_unit == 1:
            if to_unit == 1:
                inch = float(input("Enter the inches : "))
                cm = inch * 2.54
                print(f"{inch} inch is equal to {cm} cm")

            elif to_unit == 2:
                inch = float(input("Enter the inches : "))
                m = inch * 0.0254
                print(f"{inch} inch is equal to {m} m")
            else:
                print("Invalid choice")
        else:
            if to_unit == 1:
                feet = float(input("Enter the feet : "))
                cm = feet * 30.48
                print(f"{feet} feet is equal to {cm} cm")
            elif to_unit == 2:
                feet = float(input("Enter the feet : "))
                m = feet * 0.3048
                print(f"{feet} feet is equal to {m} m")
            else:
                print("Invalid choice")

    case _:
        print("Invalid choice")
