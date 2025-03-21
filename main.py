from functions import *


def main():
    tracker = FinanceTracker()

    while True:
        print('''
Menu:
1. Adding new financial transactions (income, expenses)
2. Filtering by type, by category or by amount
3. Sorting by type, by category or by amount
4. Deleting financial transactions
5. Editing financial transactions
6. Displaying all transactions
7. Exit
        ''')

        choice = int(input("Enter your choice: "))

        if choice == 1:
            transaction_amount = int(input("Enter amount of transaction: "))
            transaction_category = input("Enter category(salary, business, shop, entertainment) of transaction: ")
            transaction_type = input("Enter type(income, expenses) of transaction: ")
            print(tracker.adding_new_financial_transactions(transaction_amount, transaction_category, transaction_type))

        elif choice == 2:
            sorting = int(input("""Sorting by: 
1. Transaction amount
2. Transaction category
3. Transaction type
Enter your choice: """))
            if sorting == 1:
                sorting = "transaction_amount"
            elif sorting == 2:
                sorting = "transaction_category"
            elif sorting == 3:
                sorting = "transaction_type"
            else:
                print("Invalid choice")
                continue

            if sorting == "transaction_amount":
                value = input("Enter value of transaction amount: ")
            elif sorting == "transaction_category":
                value = input("Enter value of transaction category(salary, business, shop, entertainment): ")
            elif sorting == "transaction_type":
                value = input("Enter value of transaction type(income, expenses): ")
            else:
                print("Invalid choice")
                continue

            print(tracker.filter_all_financial_transactions(sorting, value))

        elif choice == 3:
            sorting = int(input("""Sorting by: 
1. Transaction amount
2. Transaction category
3. Transaction type
Enter your choice: """))

            if sorting == 1:
                sorting = "transaction_amount"
            elif sorting == 2:
                sorting = "transaction_category"
            elif sorting == 3:
                sorting = "transaction_type"
            else:
                print("Invalid choice")
                continue

            desc = int(input("Sorting ascending(1) or descending(2): "))
            print()
            if desc == 1:
                desc = True
            elif desc == 2:
                desc = False
            else:
                print("Invalid choice")
                continue

            print(tracker.sort_all_financial_transactions(sorting, desc))

        elif choice == 4:
            print(tracker.show_all_financial_transactions())

            index = int(input("Enter index: "))
            print(tracker.delete_financial_transactions(index))

        elif choice == 5:
            print(tracker.show_all_financial_transactions())

            index = int(input("Enter index: "))
            transaction_amount = input("Enter amount of transaction or skip: ")
            transaction_amount = transaction_amount if transaction_amount else False
            transaction_category = input("Enter category(salary, business, shop, entertainment) of transaction or skip: ")
            transaction_category = transaction_category if transaction_category else False
            transaction_type = input("Enter type(income, expenses) of transaction or skip: ")
            transaction_type = transaction_type if transaction_type else False

            print(tracker.edit_financial_transactions(index, transaction_amount, transaction_category, transaction_type))

        elif choice == 6:
            print(tracker.show_all_financial_transactions())

        elif choice == 7:
            print("Exiting...")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
