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

    def show_all_financial_transactions(self, sorting_by, descending=True):
        """Виведення списку всіх операцій з можливістю сортування за типом, за категорією чи за сумою"""
        result = sorted(self.transactions, key=lambda transactions: transactions[sorting_by])
        if descending:
            for res in result:
                print(f'{res["transaction_type"]}: {res["transaction_amount"]} - {res["transaction_category"]}')
            return "\nSorting by ascending"
        else:
            for res in reversed(result):
                print(f'{res["transaction_type"]}: {res["transaction_amount"]} - {res["transaction_category"]}')
            return "\nSorting by descending"

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
