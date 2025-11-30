def loop():
    print("Enter a formula")
    print("a - velocity = distance/ time")
    print("b - acceleration = velocity / time")
    print("c - work = force * distance")
    print("d - force = mass * acceleration")
    print("e - density = force * time")

    formula = input("Enter a, b, c, d or e: ").lower()

    if formula == "a":
        print("Velocity = distance / time")
        distance = float(input("Enter the distance : "))
        time = float(input("Enter the time : "))
        velocity = distance / time
        print("velocity = ",velocity, "m/s")
        again = input("Do you want to solve another Physics formula? (Yes/No)").lower()

        if again == "yes":
            loop()
        else:
            print("Thank you for using Physics formulas")

    elif formula == "b":
        print("acceleration = velocity / time")
        velocity = float(input("Enter the velocity : "))
        time = float(input("Enter the time : "))
        acceleration = velocity / time
        print("acceleration = ",acceleration, "m/s^2")
        again = input("Do you want to solve another Physics formula? (Yes/No)").lower()

        if again == "yes":
            loop()
        else:
            print("Thank you for using Physics formulas")
    elif formula == "c":
        print("work done = force * distance")
        force = float(input("Enter the force : "))
        distance = float(input("Enter the distance : "))
        work  = force * distance
        print("work done = ",work , "J")
        again = input("Do you want to solve another Physics formula? (Yes/No)").lower()
        if again == "yes":
            loop()
        else:
            print("Thank you for using Physics formulas")
    elif formula == "d":
        print("force = mass * acceleration")
        mass = float(input("Enter the mass : "))
        acceleration = float(input("Enter the acceleration : "))
        force = mass * acceleration
        print("force = ",force, "N")
        again = input("Do you want to solve another Physics formula? (Yes/No)").lower()

        if again == "yes":
            loop()
        else:
            print("Thank you for using Physics formulas")

    elif formula == "e":
        print("density = mass / volume")
        mass = float(input("Enter the mass :"))
        volume  = float(input("Enter the volume : "))
        density = mass / volume
        print("density =", density, "Kg/m^3")
        again = input("Do you want to solve another Physics formula? (Yes/No)").lower()

        if again == "yes":
            loop()
        else:
            print("Thank you for using Physics formulas")
    else:
        print("Invalid formula")
    loop()
loop()




