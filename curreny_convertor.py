def currency_converter():
    # Predefined exchange rates with respect to USD
    exchange_rates = {
        "EUR": 0.85,  # Euro
        "GBP": 0.75,  # British Pound
        "JPY": 110.0,  # Japanese Yen
        "AUD": 1.35,  # Australian Dollar
        "CAD": 1.25,  # Canadian Dollar
    }
    
    print("Currency Converter")
    amount = float(input("Enter the amount in USD: "))
    
    print("\nConverted amounts:")
    for currency, rate in exchange_rates.items():
        converted_amount = amount * rate
        print(f"{amount} USD = {converted_amount:.2f} {currency}")

# Run the currency converter
currency_converter()
