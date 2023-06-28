from PyExpansion.common import table
from PyExpansion.application.finance import utils


class MoneyBorrowAndPay(table.BaseTable):

    data = [
        [
            "Month", "Initial", "Pay", "Balance"
        ]
    ]

    def __init__(self, amount, pa, borrow_year, currency_symbol="RM"):
        self.amount = amount
        self.pa = pa / 100
        self.borrow_year = borrow_year
        self.currency_symbol = currency_symbol
        self.pay_month = self.borrow_year * 12
        self.adjustment = 0

    def _get_total_pay(self):
        return utils.fixed_decimal_place(self.amount * (1 + (self.pa * self.borrow_year)))

    def _pay_by_month(self):
        return utils.fixed_decimal_place(self._get_total_pay() / self.pay_month)

    def get_total_pay(self):
        return utils.currency_represent(self._get_total_pay(), currency_symbol=self.currency_symbol)

    def pay_by_month(self):
        return utils.currency_represent(self._pay_by_month(), currency_symbol=self.currency_symbol)

    def create_table(self):
        data = self.data.copy()
        total_amount = self._get_total_pay()
        pay_by_month = self._pay_by_month()
        for x in range(1, self.pay_month + 1):
            if x != self.pay_month:
                remaining_amount = total_amount - pay_by_month
            else:
                self.adjustment = total_amount - pay_by_month
                pay_by_month = total_amount
                remaining_amount = 0
            data.append([
                x, utils.currency_represent(total_amount, currency_symbol=self.currency_symbol),
                utils.currency_represent(pay_by_month, currency_symbol=self.currency_symbol),
                utils.currency_represent(remaining_amount, currency_symbol=self.currency_symbol)
            ])
            total_amount -= self._pay_by_month()
        return data

    def print_out(self, end=" "):
        print("Payment Chart: ")
        table.BaseTable.print_out(self, end=" | ")
        print()
        print("Adjustment: ", utils.currency_represent(self.adjustment, currency_symbol=self.currency_symbol))


test_MoneyBorrowAndPay = True
if test_MoneyBorrowAndPay:
    c = MoneyBorrowAndPay(5000, 24, 2)
    print("Total Pay: ", c.get_total_pay())
    print("Pay Per Month: ", c.pay_by_month())
    print()
    c.print_out()
