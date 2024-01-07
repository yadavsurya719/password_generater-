import random
import string
from termcolor import colored

def generate_random_password(length=12):
    # Define character sets for different factors
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    # Ensure the password length is at least 4 characters
    length = max(length, 4)

    # Use at least one character from each factor
    password = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Fill the rest of the password with random characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password to mix the factors
    random.shuffle(password)

    # Convert the list to a string
    password = ''.join(password)

    return password

def generate_single_code():
    # Simulating the generation of a single code
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

def main():
    try:
        print("Select the type of output:")
        print("1. Generate a password with name, numbers, and special characters")
        print("2. Generate a password consisting only of numbers")
        print("3. Generate a single code")

        choice = int(input("Enter your choice (1, 2, or 3): "))

        if choice == 1:
            name = input("Enter your name: ")
            if not name:
                raise ValueError("Name should not be empty.")
            password = generate_random_password(len(name) + 8)
            colored_output = colored(f"Generated Password: {password}", "green")
        elif choice == 2:
            password_length = int(input("Enter the desired password length: "))
            password = generate_random_password(password_length)
            colored_output = colored(f"Generated Password: {password}", "blue")
        elif choice == 3:
            password = generate_single_code()
            colored_output = colored(f"Generated Code: {password}", "yellow")
        else:
            raise ValueError("Invalid choice. Please enter 1, 2, or 3.")

        print(colored_output)

    except ValueError as e:
        print(colored(f"Error: {e}", "red2"))

if __name__ == "__main__":
    main()
