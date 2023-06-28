def currency_represent(amount, currency_symbol="", decimal_place=2, have_separator=False, change_place=False):
    """
    :param amount: figure
    :param currency_symbol: symbol of the figure
    :param decimal_place: number after '.'
    :param have_separator: use for easy read figure
    :param change_place: switch the symbol of decimal place and separator
    :return:
    """
    currency_pattern = currency_symbol
    currency_pattern += "{:"
    currency_pattern += "," if have_separator else ""
    currency_pattern += "."
    currency_pattern += str(decimal_place) if decimal_place > 0 else 2
    currency_pattern += "f}"
    word = currency_pattern.format(amount)
    if change_place:
        front, back = word.split(".")
        front = front.replace(",", ".")
        word = front + "," + back
    return word


def fixed_decimal_place(amount, decimal_places=2):
    return int(amount * 10 ** decimal_places) / 10 ** decimal_places


# print(currency_represent(2000, currency_symbol="RM", have_separator=True, change_place=False))
