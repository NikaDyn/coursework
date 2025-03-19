class FinanceTracker:
    def __init__(self):
        self.transactions = []

    def adding_new_financial_transactions(self, transaction_amount, transaction_category, transaction_type):
        """Додавання нових фінансових операцій (доходи, витрати)"""
        self.transactions.append({
            "transaction_amount": transaction_amount,
            "transaction_category": transaction_category,
            "transaction_type": transaction_type,
        })
        return "Transactions was added"

    def show_all_financial_transactions(self):
        if self.transactions:
            for t in self.transactions:
                print(f'{self.transactions.index(t)}. {t["transaction_type"]}: {t["transaction_amount"]} - {t["transaction_category"]}')
            return ''
        else:
            return "There is no transactions"

    def sort_all_financial_transactions(self, sorting_by, value):
        """Виведення списку всіх операцій з можливістю сортування за типом, за категорією чи за сумою"""
        if sorting_by == "transaction_amount":
            trans_list = [i for i in self.transactions if i["transaction_amount"] == int(value)]

            if trans_list:
                for t in trans_list:
                    print(f'{t["transaction_type"]}: {t["transaction_amount"]} - {t["transaction_category"]}')
                return ''
            else:
                return f"There are no {value} transaction amount"

        elif sorting_by == "transaction_category":
            trans_list = [i for i in self.transactions if i["transaction_category"] == value]

            if trans_list:
                for t in trans_list:
                    print(f'{t["transaction_type"]}: {t["transaction_amount"]} - {t["transaction_category"]}')
                return ''
            else:
                return f"There are no {value} transaction category"

        elif sorting_by == "transaction_type":
            trans_list = [i for i in self.transactions if i["transaction_type"] == value]

            if trans_list:
                for t in trans_list:
                    print(f'{t["transaction_type"]}: {t["transaction_amount"]} - {t["transaction_category"]}')
                return ''
            else:
                return f"There are no {value} transaction type"

        else:
            return f'We can not sort by {sorting_by}'

    def edit_financial_transactions(self, index, transaction_amount=False, transaction_category=False, transaction_type=False):
        """редагування фінансових операцій"""
        if 0 <= index <= len(self.transactions):
            if transaction_amount:
                self.transactions[index]["transaction_amount"] = transaction_amount
            if transaction_category:
                self.transactions[index]["transaction_category"] = transaction_category
            if transaction_type:
                self.transactions[index]["transaction_type"] = transaction_type

            return "Transaction was edited"
        else:
            return "There is no such transaction"

    def delete_financial_transactions(self, index):
        """видалення фінансових операцій"""
        if 0 <= index <= len(self.transactions):
            self.transactions.pop(index)
            return "Transaction was deleted"
        else:
            return "There is no such transaction"
