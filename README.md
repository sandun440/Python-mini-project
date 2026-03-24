# Bank Management System

A simple **Python console-based Bank Management System** that allows users to create bank accounts and perform basic banking operations such as checking balance, depositing money, withdrawing money, and transferring money between accounts.

## Features

- Create a new bank account
- Check account balance
- Deposit money
- Withdraw money
- Transfer money to another account
- Menu-driven console interface

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP)

## Project Structure

This project uses a single Python class:

- `Bank` class
  - Stores account details in a dictionary
  - Provides all banking operations through class methods

## How It Works

The system stores account numbers and balances in a dictionary:

```python
self.bank_details = {}
```

Each account number is generated randomly, and the balance is stored as the account value.

## Menu Options

When you run the program, you will see the following options:

1. Create an account
2. Check balance
3. Deposit money
4. Withdraw money
5. Transfer money
6. Exit

## Requirements

- Python 3.x installed on your computer

## How to Run

1. Copy the Python code into a file named `bank.py`
2. Open terminal or command prompt
3. Run the program:

```bash
python bank.py
```

## Example Usage

### Create Account
- Enter the initial deposit amount
- The system generates a random account number
- Your account is created successfully

### Check Balance
- Enter your account number
- The system displays your current balance

### Deposit Money
- Enter your account number
- Enter deposit amount
- The balance updates

### Withdraw Money
- Enter your account number
- Enter withdrawal amount
- The system checks if enough balance is available

### Transfer Money
- Enter your account number
- Enter receiver account number
- Enter transfer amount
- Money is transferred if balance is sufficient

## Concepts Used

- Classes and Objects
- Dictionaries
- Functions/Methods
- Conditional Statements
- Loops
- User Input Handling
- Random Number Generation

## Limitations

- Data is not saved permanently
- All account details are lost when the program stops
- No password/login security
- Account number generation may rarely create duplicates
- Limited error handling

## Future Improvements

- Add file handling or database storage
- Add PIN/password protection
- Improve validation and exception handling
- Add transaction history
- Add interest calculation
- Build a GUI or web version

## Author

Developed as a beginner-friendly Python banking project for learning purposes.

## License

This project is free to use for educational purposes.
