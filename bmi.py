def calculate_bmi(weight, height):
    """
    Calculate BMI (Body Mass Index)
    :param weight: weight in kilograms
    :param height: height in meters
    :return: BMI value
    """
    return weight / (height ** 2)

def get_bmi_category(bmi):
    """
    Get BMI category based on BMI value
    :param bmi: BMI value
    :return: category string
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

if __name__ == "__main__":
    print("BMI Calculator")
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))
        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)
        print(f"Your BMI is: {bmi:.2f}")
        print(f"Category: {category}")
    except ValueError:
        print("Please enter valid numbers for weight and height.")

