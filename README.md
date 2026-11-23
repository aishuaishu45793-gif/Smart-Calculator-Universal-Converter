# 🧮 Smart Calculator & Universal Converter

A Python-based application that combines basic arithmetic, scientific calculations, and unit conversions in one place. It provides a simple menu-driven interface and separates functionality into individual Python modules for easier maintenance and future development.

## 🚀 Features

### 1. Basic Calculator
- Addition
- Subtraction
- Multiplication
- Division
- Modulus
- Power
- Percentage

### 2. Scientific Calculator
- Square root
- Factorial
- Sine
- Cosine
- Tangent
- Logarithm (base 10)
- Natural logarithm

### 3. Unit Converter

**Length**
- Kilometers to Miles
- Miles to Kilometers
- Meters to Feet
- Feet to Meters
- Centimeters to Inches
- Inches to Centimeters

**Weight**
- Kilograms to Pounds
- Pounds to Kilograms
- Grams to Kilograms
- Kilograms to Grams

**Temperature**
- Celsius to Fahrenheit
- Fahrenheit to Celsius
- Celsius to Kelvin
- Kelvin to Celsius

### 4. Additional Features
- Menu-driven command-line interface
- Input validation
- Error handling for invalid calculations
- Modular project structure

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Libraries:** Python standard library
- **Database:** SQLite (planned)
- **Version Control:** Git and GitHub

## 📁 Project Structure

```text
Smart-Calculator-Universal-Converter/
│
├── calculator/
│   ├── __init__.py
│   ├── basic.py
│   ├── scientific.py
│   └── interface.py
│
├── converters/
│   ├── __init__.py
│   ├── length.py
│   ├── weight.py
│   ├── temperature.py
│   └── interface.py
│
├── utils/
│   ├── __init__.py
│   └── validators.py
│
├── modules/
│
├── config.py
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### Step 1: Clone the repository

```bash
git clone https://github.com/aishuaishu45793-gif/Smart-Calculator-Universal-Converter.git
```

### Step 2: Navigate to the project folder

```bash
cd Smart-Calculator-Universal-Converter
```

### Step 3: Create a virtual environment

```bash
python -m venv .venv
```

### Step 4: Activate the virtual environment

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

**Windows Command Prompt:**

```cmd
.venv\Scripts\activate
```

### Step 5: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Run the application

```bash
python main.py
```

## 💻 How to Use

1. Run the application using `python main.py`.
2. Select an option from the main menu.
3. Choose the required calculation or conversion.
4. Enter the requested number or values.
5. View the result in the terminal.
6. Return to the main menu to perform another operation.

## 🔮 Future Enhancements

The following features are planned for future versions:

- Live currency conversion using exchange-rate APIs
- SQLite-based calculation history
- Export calculation history to CSV
- Save and manage favorite calculations
- Automated unit testing
- Improved user interface

## 🎯 Project Objective

The main objective of this project is to develop a reusable Python application that combines mathematical calculations and common unit conversions. It also demonstrates modular programming, functions, exception handling, input validation, and project organization.

## 👩‍💻 Developer

**Aishwarya**

## 🔗 GitHub Repository

[Smart Calculator & Universal Converter](https://github.com/aishuaishu45793-gif/Smart-Calculator-Universal-Converter)

## 📄 License

This project is open-source and available for learning and educational purposes. Add a formal license file if you want to specify reuse and distribution permissions.

---

⭐ If you find this project useful, consider giving the repository a star!
