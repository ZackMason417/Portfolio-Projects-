def calculate_bmi(weight, height):
    """
    Calculate the Body Mass Index (BMI) using weight in kilograms and height in meters.

    Parameters:
    - weight: Weight in kilograms (float)
    - height: Height in meters (float)

    Returns:
    - BMI (float)
    """
    return weight / height**2


def interpret_bmi(bmi):
    """
    Interpret the BMI value and provide a classification.

    Parameters:
    - bmi: Body Mass Index (float)

    Returns:
    - Classification string
    """
    if bmi < 18.5:
        return "Underweight"
    elif bmi <= 24.9:
        return "Normal Weight"
    elif bmi <= 29.9:
        return "Overweight"
    elif bmi <= 34.9:
        return "Obese"
    elif bmi <= 39.9:
        return "Severely Obese"
    else:
        return "Morbidly Obese"


def main():
    name = input("Enter your name: ")
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    bmi = calculate_bmi(weight, height)

    print("\nCalculating BMI...\n")
    print("Name:", name)
    print("Weight:", weight, "kg")
    print("Height:", height, "m")
    print("BMI:", round(bmi, 2))

    bmi_classification = interpret_bmi(bmi)
    print(name + ", you are " + bmi_classification + ".")


if __name__ == "__main__":
    main()
