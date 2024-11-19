# Currency Converter Project

### Author: Sabrina Joseph  
### Date: 01-24-2024  
### Last Modified: 01-24-2024

## Description
This Python script is part of the Module 2 Lab Activity C and serves as a simple currency converter. The program allows users to convert a specified amount of currency between three options: USD (United States Dollar), CAD (Canadian Dollar), and YEN (Japanese Yen). The user inputs the amount, the original currency, and the desired currency to convert to, and the program returns the converted value.

## Features
- Supports conversion between USD, CAD, and YEN.
- Conversion rates:
  - USD to CAD: 1 USD = 1.24 CAD
  - USD to YEN: 1 USD = 108.59 YEN
  - CAD to USD: 1 CAD = 1 / 1.24 USD
  - CAD to YEN: 1 CAD = (1 / 1.24) * 108.59 YEN
  - YEN to USD: 1 YEN = 1 / 108.59 USD
  - YEN to CAD: 1 YEN = (1 / 108.59) * 1.24 CAD

## How to Use
1. Run the script in a Python environment.
2. The program will display the available currencies: A) USD, B) CAD, C) YEN.
3. Enter the transaction amount you wish to convert.
4. Select the original currency by typing:
   - A for USD
   - B for CAD
   - C for YEN
5. Select the currency you want to convert to by typing:
   - A for USD
   - B for CAD
   - C for YEN
6. The program will display the converted amount based on the selected currencies.

## Example Usage
```plaintext
Available currencies: A)USD B)CAD C)YEN
Enter transaction amount: 100
Transaction currency: A
Currency to convert to: B
Converted value: 124.0 CAD
```

This project is licensed under the MIT License. See the LICENSE file for details.
