def loop():
    print("select a formula")
    print("a - velocity= distance / time")
    print("b - force= mass * acceleration")
    print("c - pressure= force / area")
    print("d - density = mass / volume")
    print("e - moment = Force * Perpendicular Distance")

    formula = input("Enter one of the following a, b, c, d or e: ").lower()

    if formula == "a":
        print("Velocity = distance / time")
        distance = float(input("Enter the distance : "))
        time = float(input("Enter the time : "))
        velocity = distance / time
        print("velocity = ",velocity, "m/s")
        rerun = input("Do you want to solve another problem? (yes/no): ").lower()
        if rerun == "yes":
            loop()
        if rerun == "no":
            print("Thank you for using Physics Formulas")

    elif formula == "b":
        print("Force = mass * acceleration")
        mass = float(input("Enter the mass : "))
        acceleration = float(input("Enter the acceleration : "))
        force = mass * acceleration
        print("force = ",force, "kgm/s^2")
        rerun = input("Do you want to to solve another problem? (yes/no): ").lower()
        if rerun == "yes":
            loop()
        if rerun == "no":
            print("Thank you for using Physics Formulas")


    elif formula == "c":
        print("Pressure = force / area")
        force = float(input("Enter the force : "))
        area = float(input("Enter the area : "))
        pressure = force / area
        print("pressure = ",pressure, "N/m^2")
        rerun = input("Do you want to to solve another problem? (yes/no): ").lower()
        if rerun == "yes":
            loop()
        if rerun == "no":
            print("Thank you for using Physics Formulas")



    elif formula == "d":
        print("Density = mass / volume")
        mass = float(input("Enter the mass : "))
        volume = float(input("Enter the volume : "))
        density = mass / volume
        print("density = ",density, "kg/m^3")
        rerun = input("Do you want to to solve another problem? (yes/no): ").lower()
        if rerun == "yes":
            loop()
        if rerun == "no":
            print("Thank you for using Physics Formulas")



    elif formula == "e":
        print("Moment = Force * Perpendicular Distance")
        force = float(input("Enter the force : "))
        perpendicular_distance = float(input("Enter the perpendicular distance : "))
        moment = force * perpendicular_distance
        print("moment =", moment, "N/m")
        rerun = input("Do you want to to solve another problem? (yes/no): ").lower()
        if rerun == "yes":
            loop()
        if rerun == "no":
            print("Thank you for using Physics Formulas")


    else:
        print("Invalid formula. Please select any of the following: a, b, c, d, e.")
        loop()

loop()











