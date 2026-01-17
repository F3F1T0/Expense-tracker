# Expense Tracker CLI

A lightweight and efficient Command Line Interface (CLI) tool to manage your daily expenses. This project implements a full CRUD (Create, Read, Update, Delete) system using Python's standard library and CSV files for data persistence.

## 🚀 Key Features & Engineering Highlights

This project was built focusing on software architecture and data integrity:
- **CSV Persistence**: Uses Python's `csv` module to store and manage data.
- **Atomic File Operations**: Implements a "Load-Modify-Overwrite" pattern to ensure data consistency during updates and deletions.
- **Smart ID Management**: Includes an auto-incrementing ID system that calculates the next ID based on the maximum existing record, preventing ID collisions.
- **Modular Design**: Clear separation of concerns between the interface layer (`main.py`) and the data engine (`expenses.py`).
- **Input Validation**: Robust handling of data types (floats for currency, integers for months) and filtering of potential header corruption.

## 🛠️ Requirements & Installation

1. Ensure you have **Python 3.10** or higher installed.
2. Download or clone this repository containing `main.py` and `expenses.py`.
3. No external dependencies are required (Built entirely with Python's Standard Library).

## 📖 Usage Guide

### 1. Add a New Expense
```bash
python main.py add --description "Coffee" --amount 4.50
``` 
### 2. List All Expenses

Displays a clean, formatted table in your terminal:
``` Bash

python main.py list
``` 
### 3. Update an Expense

Modify the amount of an existing entry by its unique ID:
``` Bash

python main.py update --id 1 --amount 5.25
``` 
### 4. Delete an Expense

Permanently remove a record from the database:
```  Bash

python main.py delete --id 1
``` 
### 5. Financial Summary

    Total Balance:
```     Bash

    python main.py summary
``` 
    Filter by Month (e.g., 1 for January):
```     Bash

    python main.py summary --month 1
``` 
## 🧠 Project Architecture

The application follows a modular structure:

    main.py: The entry point. Handles CLI argument parsing via argparse and routes commands.

    expenses.py: The core logic. Manages CSV I/O, ID generation, and mathematical summaries.

    expenses.csv: The flat-file database (automatically initialized on first run).

### Credits
This project has been made following the project of: https://roadmap.sh/projects/expense-tracker
