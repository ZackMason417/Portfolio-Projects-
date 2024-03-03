name = input("Enter your name: ")

weight = float(input("Enter your weight in kilograms: "))

height = float(input("Enter your height in meters: "))

BMI = weight / height**2

print("\nCalculating BMI...\n")
print("Name:", name)
print("Weight:", weight, "kg")
print("Height:", height, "m")
print("BMI:", round(BMI, 2))

if BMI > 0:
    if BMI < 18.5:
        print(name + ", you are Underweight.")
    elif BMI <= 24.9:
        print(name + ", you are Normal Weight.")
    elif BMI <= 29.9:
        print(name + ", you are Overweight.")
    elif BMI <= 34.9:
        print(name + ", you are Obese.")
    elif BMI <= 39.9:
        print(name + ", you are Severely Obese.")
    elif BMI > 40:
        print(name + ", you are Morbidly Obese.")
    else:
        print(name + ", Please enter valid input.")
