EMPLOYEES = [
    {
        "id": 1,
        "name": "Jenna Solis"
    }
]

# Function with a single parameter
def get_single_employee(id):
    """Variable to hold the found employee, if it exists"""
    requested_employee = None

    # Iterate the LOCATIONS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee


def get_all_employees():
    """Function returning employees."""
    return EMPLOYEES
