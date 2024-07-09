# pylint: disable=missing-docstring

RATES = {
    'USDEUR' : 0.85,
    'GBPEUR' : 1.13,
    'CHFEUR' : 0.86,
    'EURGBP' : 0.885,
}

def convert(amount, currency):
    """returns the converted amount in the given currency
    amount is a tuple like (100, "EUR")
    currency is a string
    """
    converter = amount[1]+currency
    return round(amount[0]*RATES[converter],0) if converter in RATES else None

print(convert((100, "EUR"), "USD"))
