
# Password Generator

A simple and customizable password generator written in Python. This tool creates secure, random passwords based on user-defined criteria such as length, inclusion of uppercase letters, numbers, and special characters. 

## Features

- **Customizable Length**: Define the desired length of the password (minimum 4 characters).
- **Inclusion Options**:
  - Uppercase letters
  - Numbers
  - Special characters (e.g., `!@#$%^&*`)
- **Random and Secure**: Ensures the password is randomized and includes at least one character from each selected category.
- **Interactive Interface**: Allows users to input their preferences interactively.

## Prerequisites

- Python 3.6 or later

## Installation

1. Clone this repository or copy the `password_generator.py` file into your project:
   ```bash
   git clone https://github.com/Goldenhubuz/password-generator.git
   cd password-generator
   ```

2. Ensure Python is installed on your system. You can check by running:
   ```bash
   python --version
   ```

## Usage

### Run the Script
Run the script using Python:
```bash
python password_generator.py
```

### Interactive Options
The script will prompt you for the following inputs:
1. **Password Length**: Specify the length of the password (default is 12).
2. **Include Uppercase Letters**: Choose whether to include uppercase letters (default is `yes`).
3. **Include Numbers**: Choose whether to include numbers (default is `yes`).
4. **Include Special Characters**: Choose whether to include special characters (default is `yes`).

### Example Output
```plaintext
Password Generator
Enter password length (default is 12): 16
Include uppercase letters? (y/n, default is y): y
Include numbers? (y/n, default is y): y
Include special characters? (y/n, default is y): n
Generated Password: tZqvmJr84XyPwkLf
```

### Direct Function Usage
You can also use the `generate_password` function directly in your own Python code:
```python
from password_generator import generate_password

password = generate_password(length=16, include_uppercase=True, include_numbers=True, include_special=False)
print(f"Generated Password: {password}")
```

## Error Handling

- If the specified password length is less than 4, the program will raise an error:
  ```plaintext
  Error: Password length must be at least 4 characters.
  ```
- If no character types are selected, an error will occur:
  ```plaintext
  Error: At least one character type must be included.
  ```

## Customization

You can further customize the character sets or logic by modifying the following variables in the script:
- `string.ascii_lowercase`: Lowercase letters
- `string.ascii_uppercase`: Uppercase letters
- `string.digits`: Numbers
- `string.punctuation`: Special characters

## Contributing

Feel free to fork this project, create feature requests, or submit pull requests. Contributions are welcome!

## License

This project is licensed under the GPL License. See the `LICENSE` file for details.

## Contact

For any questions or feedback, please feel free to [email me](mailto:goldendevuz@gmail.com).

---

Enjoy using the Password Generator, and happy securing your accounts!