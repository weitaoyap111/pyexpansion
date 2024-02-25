import random

from PyExpansion.common.constants import common


class PasswordGenerator(object):

    def __init__(self, length=6, include_number=True, include_symbol=True, include_lower=True, include_capital=True):
        self.length = length
        self.include_number = include_number
        self.include_symbol = include_symbol
        self.include_capital = include_capital
        self.include_lower = include_lower

    @property
    def generate(self):
        password_template = ""
        if self.include_lower:
            password_template += common.LOWER_ABC
        if self.include_capital:
            password_template += common.CAPITAL_ABC
        if self.include_number:
            password_template += common.NUMBER
        if self.include_symbol:
            password_template += common.SYMBOL

        password = ''.join([random.choice(password_template) for i in range(self.length)])
        return password
