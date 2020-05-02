from forex_python.converter import CurrencyRates

schmeckle_amount = input("Enter schmeckle amount: \n")
currency = input("Enter currency to exchange to: \n").upper()

schmeckle_float = float(schmeckle_amount)
schmeckle_converted = schmeckle_float*148

currency_rate = CurrencyRates().get_rate('USD', currency)
usd_to_currency = round(float(schmeckle_converted*currency_rate), 2)
print(f"{schmeckle_float} schmeckles in {currency} is {usd_to_currency}")
