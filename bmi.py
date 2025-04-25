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

def calculate_ideal_weight(height, target_bmi=22):
    """
    Calculate ideal weight for given height and target BMI
    :param height: height in meters
    :param target_bmi: target BMI value (default 22)
    :return: ideal weight in kg
    """
    return target_bmi * (height ** 2)

def validate_input(weight, height):
    """
    Validate weight and height inputs
    :param weight: weight in kg
    :param height: height in meters
    :return: tuple of (is_valid, error_message)
    """
    if weight <= 0 or height <= 0:
        return False, "Weight and height must be positive numbers"
    if height < 0.5 or height > 2.5:
        return False, "Height should be between 0.5 and 2.5 meters"
    if weight < 2 or weight > 300:
        return False, "Weight should be between 2 and 300 kg"
    return True, ""

if __name__ == "__main__":
    print("BMI Calculator")
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))    
        is_valid, error_msg = validate_input(weight, height)
        if not is_valid:
            print(f"Error: {error_msg}")
            exit(1)        
        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)
        ideal_weight = calculate_ideal_weight(height)
        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Category: {category}")
        print(f"Ideal weight for your height: {ideal_weight:.2f} kg")
        print(f"Difference: {weight - ideal_weight:.2f} kg")
    except ValueError:
        print("Error: Please enter valid numbers for weight and height")
