import os
from datetime import datetime
import csv 


def add_expense(desc, amount):
    # Calculate ID
    FILE = "expenses.csv"
    new_id = 1
    if os.path.exists(FILE):
        with open(FILE, mode='r') as f:
            reader = csv.DictReader(f)

            # Search for max ID
            ids = []
            for row in reader:
                valor_id_texto = row['id']    # Sacamos el ID (viene como texto: "1")
                valor_id_numero = int(valor_id_texto) # Lo pasamos a número
                ids.append(valor_id_numero)   # Lo guardamos en nuestra lista

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

        writer.writeheader()

        writer.writerow(new_expense)   

    print(f"The expense has been created succesfully. ID: {new_expense['id']}")

