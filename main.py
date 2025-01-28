import random
import string

def generate_password(length=12, include_uppercase=True, include_numbers=True, include_special=True):
    """
    Generate a random secure password based on user-defined criteria.

    Args:
        length (int): Length of the password (default is 12).
        include_uppercase (bool): Include uppercase letters (default is True).
        include_numbers (bool): Include numbers (default is True).
        include_special (bool): Include special characters (default is True).

    Returns:
        str: The generated password.
    """

    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")

    # Define the character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase else ""
    numbers = string.digits if include_numbers else ""
    special = string.punctuation if include_special else ""

    # Ensure at least one character from each selected category
    all_characters = lowercase + uppercase + numbers + special
    if not all_characters:
        raise ValueError("At least one character type must be included.")

    # Select at least one character from each pool (if applicable)
    password = []
    if include_uppercase:
        password.append(random.choice(uppercase))
    if include_numbers:
        password.append(random.choice(numbers))
    if include_special:
        password.append(random.choice(special))
    password.append(random.choice(lowercase))

    # Fill the rest of the password length with random choices
    while len(password) < length:
        password.append(random.choice(all_characters))

    # Shuffle to ensure randomness
    random.shuffle(password)

    return ''.join(password)


# Example usage
if __name__ == "__main__":
    print("Password Generator")
    length = int(input("Enter password length (default is 12): ") or 12)
    include_uppercase = input("Include uppercase letters? (y/n, default is y): ").lower() != 'n'
    include_numbers = input("Include numbers? (y/n, default is y): ").lower() != 'n'
    include_special = input("Include special characters? (y/n, default is y): ").lower() != 'n'

    try:
        password = generate_password(length, include_uppercase, include_numbers, include_special)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(f"Error: {e}")