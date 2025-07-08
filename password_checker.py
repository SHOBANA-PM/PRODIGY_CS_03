import re

def check_password_strength(password):
    length_error = len(password) < 8
    lowercase_error = re.search(r"[a-z]", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = [length_error, lowercase_error, uppercase_error, digit_error, special_char_error]

    if all(not err for err in errors):
        return "Strong 💪"
    elif sum(errors) == 1:
        return "Moderate 🛡️"
    else:
        return "Weak ⚠️"

# Main program
print("🔐 Password Strength Checker")
user_password = input("Enter your password: ")
strength = check_password_strength(user_password)
print(f"Strength: {strength}")
