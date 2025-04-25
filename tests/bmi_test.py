import pytest
from bmi import calculate_bmi, get_bmi_category, calculate_ideal_weight, validate_input

def test_calculate_bmi():
    assert round(calculate_bmi(70, 1.75), 2) == 22.86

def test_get_bmi_category():
    assert get_bmi_category(17) == "Underweight"
    assert get_bmi_category(22) == "Normal weight"
    assert get_bmi_category(27) == "Overweight"
    assert get_bmi_category(31) == "Obese"

def test_calculate_ideal_weight():
    assert round(calculate_ideal_weight(1.75), 2) == 67.38

def test_validate_input():
    assert validate_input(70, 1.75) == (True, "")
    assert validate_input(-70, 1.75)[0] is False
    assert validate_input(70, -1.75)[0] is False
    assert validate_input(70, 0.4)[0] is False
    assert validate_input(70, 3.0)[0] is False
    assert validate_input(1, 1.75)[0] is False
    assert validate_input(400, 1.75)[0] is False
    assert validate_input(500, 1.75)[0] is False