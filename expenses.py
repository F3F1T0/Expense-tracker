import os
from datetime import datetime
import csv 


FILE = "expenses.csv"
# Function of add expense

def load_expenses():
    if os.path.exists(FILE):
        with open(FILE, 'r') as file:
            csv_reader = csv.DictReader(file) # Create Dictreader to read rows

            expenses_list = [] # List that we use to store the data

            # Iterate to save the data in the list
            for row in csv_reader:
                expenses_list.append(row)
                
            return expenses_list



def add_expense(desc, amount):
    # Calculate ID
    new_id = 1
    if os.path.exists(FILE):
        with open(FILE, mode='r') as f:
            reader = csv.DictReader(f)

            # Search for max ID
            ids = []
            for row in reader:
                valor_id_texto = row['id']
                
                # 1. Filtramos: ¿Es realmente un número?
                if valor_id_texto and valor_id_texto.isdigit(): 
                    ids.append(int(valor_id_texto))

            # 2. Ahora que tenemos la lista limpia, buscamos el más grande
            if ids:
                new_id = max(ids) + 1


    # Create expense

    new_expense = {
        "description": desc,
        "amount": amount,
        "id": new_id,
        "date": datetime.now().strftime("%d-%m-%y")

    }

    # Save expense
    fields = ['description', 'amount', 'id', 'date']

    with open(FILE, 'a') as csvfile:
        
        writer = csv.DictWriter(csvfile, fieldnames = fields)

        if csvfile.tell() == 0:
            writer.writeheader()

        writer.writerow(new_expense)   
        
    csvfile.close()
    print(f"The expense has been created succesfully. ID: {new_expense['id']}")

# List expenses
def list_expenses():
    if os.path.exists(FILE):
        expenses_list = load_expenses()

        # Now we print it 
        print("\nListing expenses... ")

        print(f"{'ID':<5} {'Date':<12} {'Description':<20} {'Amount':<10}")
        for expense in expenses_list:
            print(f"{expense['id'] :<5} {expense['date']:<12} {expense['description']:<20} {expense['amount']:<10}   ")    


    else:
        print("There aren't any expenses to list. Try to add an expenses with the command 'add'")

def summary_expenses(month):
    if os.path.exists(FILE):
        expenses_list = load_expenses()
        total = 0
        if month is None:
            for i in expenses_list:
                total = total + float(i['amount'])
        else:
            for i in expenses_list:
                date = i['date'].split('-')
                expense_month = int(date[1])

                if expense_month == month:
                    total = total + float(i['amount'])
 
        
        print(f"\nTotal expenses: {total}")

    else:
        print(f"There aren't any expenses at the moment")




