import expenses 
import argparse 


def main():
    parser = argparse.ArgumentParser(prog="main.py")
    subparsers = parser.add_subparsers(dest="command")

    # Add command 
    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("--description",required=True,help="Description of the expense")
    add_parser.add_argument("--amount",required=True,type=float,help="Amount of the expense")

    # List command
    list_parser = subparsers.add_parser("list", help="List the expenses")
    
    # Update and Delete command
    del_parser = subparsers.add_parser("delete", help="Delete an expense")
    del_parser.add_argument("--id", type=int,required=True, help="id of the expense")

    upd_parser = subparsers.add_parser("update", help="Updata data of an expense")
    upd_parser.add_argument("--id", type=int,required=True, help="id of the expense")
    upd_parser.add_argument("--amount",required=True,type=float,help="Amount of the expense")

    # Summarize
    sum_parser = subparsers.add_parser("summary",help="Summarize the expenses")
    sum_parser.add_argument("--month",required=False,type=int,help="Add month to summarize")

    

    
    
    args = parser.parse_args()
    match args.command:
        case "add":
            expenses.add_expense(args.description, args.amount)
        case "list":
            expenses.list_expenses()
        case "update":
            pass
        case "delete":
            pass
        case "summary":
            expenses.summary_expenses(args.month)
        case _:
            print("That argument is not valid.")
    
if __name__ == "__main__":
    main()