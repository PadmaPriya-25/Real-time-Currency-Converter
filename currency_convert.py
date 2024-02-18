from forex_python.converter import CurrencyRates, RatesNotAvailableError

# Step 3: Accept User Input
amount = float(input("Enter the amount of money: "))
from_currency = input("Enter the currency you want to convert from (e.g., USD): ").upper()
to_currency = input("Enter the currency you want to convert to (e.g., INR): ").upper()

# Step 4: Fetch Real-time Exchange Rates with a specific source
c = CurrencyRates()
try:
    exchange_rate = c.get_rate(from_currency, to_currency)

    # Step 5: Perform Currency Conversion
    converted_amount = amount * exchange_rate

    # Step 6: Display Result
    print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")

except RatesNotAvailableError as e:
     print("Currency rates source not ready. Please try again later.")
