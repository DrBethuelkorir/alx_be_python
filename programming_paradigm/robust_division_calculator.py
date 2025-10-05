# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Safely performs division between two numbers.
    Handles:
        - Non-numeric inputs
        - Division by zero
    Returns:
        - Result message string
    """
    try:
        # Convert inputs to float
        num = float(numerator)
        den = float(denominator)

        # Perform division
        result = num / den
        return f"The result of the division is {result}"

    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
