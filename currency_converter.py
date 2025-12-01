import requests
from datetime import datetime
from typing import Dict, List, Optional

class CurrencyConverter:
    "A professional currency converter using real-time exchange rates."""
    
    BASE_URL = "https://api.exchangerate-api.com/v4/latest/"
    
    # Fallback rates for offline mode
    FALLBACK_RATES = {
        "USD": 1.0,
        "EUR": 0.92,
        "GBP": 0.79,
        "JPY": 149.50,
        "CAD": 1.32,
        "AUD": 1.53,
        "CHF": 0.88,
        "CNY": 7.24,
        "INR": 83.12,
        "MXN": 17.05
    }
    
    def __init__(self):
        self.rates = {}
        self.base_currency = "USD"
        self.last_updated = None
        
    def fetch_rates(self, base: str = "USD") -> bool:
        """ Fetch exchange rates from API."""
        try:
            response = requests.get(f"{self.BASE_URL}{base}", timeout=5)
            response.raise_for_status()
            data = response.json()
            
            self.rates = data.get("rates", {})
            self.base_currency = base
            self.last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return True
        except requests.exceptions.RequestException:
            print("⚠️  Unable to fetch rates. Using offline rates...")
            self.rates = self.FALLBACK_RATES.copy()
            self.base_currency = "USD"
            return False
    
    def convert(self, amount: float, from_currency: str, to_currency: str) -> Optional[float]:
        """Convert amount from one currency to another."""
        if not self.rates:
            return None
        
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()
        
        if from_currency not in self.rates and from_currency != self.base_currency:
            return None
        if to_currency not in self.rates and to_currency != self.base_currency:
            return None
        
        if from_currency == self.base_currency:
            rate_from = 1.0
        else:
            rate_from = self.rates[from_currency]
        
        if to_currency == self.base_currency:
            rate_to = 1.0
        else:
            rate_to = self.rates[to_currency]
        
        return (amount / rate_from) * rate_to
    
    def get_rate(self, from_currency: str, to_currency: str) -> Optional[float]:
        """Get exchange rate between two currencies."""
        converted = self.convert(1.0, from_currency, to_currency)
        return converted
    
    def get_all_currencies(self) -> List[str]:
        """Get list of all supported currencies."""
        currencies = list(self.rates.keys())
        currencies.insert(0, self.base_currency)
        return sorted(set(currencies))

def display_menu() -> int:
    """Display main menu and get user choice."""
    print("\n" + "="*50)
    print("   CURRENCY CONVERTER")
    print("="*50)
    print("1. Convert Currency")
    print("2. View Exchange Rates")
    print("3. List All Currencies")
    print("4. Update Rates")
    print("5. Exit")
    print("="*50)
    
    try:
        choice = int(input("\nSelect an option (1-5): "))
        return choice
    except ValueError:
        print("❌ Invalid input. Please enter a number 1-5.")
        return 0

def main():
    """Main program loop."""
    converter = CurrencyConverter()
    
    print("\n🌍 Welcome to Professional Currency Converter!")
    print("="*50)
    print("Fetching latest exchange rates...")
    
    if converter.fetch_rates():
        print("✓ Rates updated successfully (Base: USD)")
    else:
        print("✓ Using offline rates")
    
    while True:
        choice = display_menu()
        
        if choice == 1:
            # Convert Currency
            try:
                amount = float(input("\nEnter amount: "))
                from_curr = input("From currency (e.g., USD): ").upper()
                to_curr = input("To currency (e.g., EUR): ").upper()
                
                result = converter.convert(amount, from_curr, to_curr)
                if result is not None:
                    print(f"\n✓ {amount} {from_curr} = {result:.2f} {to_curr}")
                else:
                    print("❌ Currency not found or conversion failed.")
            except ValueError:
                print("❌ Invalid input. Please enter a valid amount.")
        
        elif choice == 2:
            # View Exchange Rates
            from_curr = input("\nEnter base currency (e.g., USD): ").upper()
            print(f"\nExchange rates for {from_curr}:")
            print("-" * 40)
            for currency, rate in list(converter.rates.items())[:10]:
                print(f"  {currency}: {rate:.4f}")
            print(f"\n  (Last updated: {converter.last_updated})")
        
        elif choice == 3:
            # List All Currencies
            currencies = converter.get_all_currencies()
            print(f"\n✓ {len(currencies)} currencies supported:")
            print("-" * 40)
            for i, curr in enumerate(currencies, 1):
                print(f"  {curr}", end="  ")
                if i % 10 == 0:
                    print()
            print()
        
        elif choice == 4:
            # Update Rates
            print("\nUpdating exchange rates...")
            if converter.fetch_rates():
                print("✓ Rates updated successfully!")
            else:
                print("⚠️  Could not update rates. Check your connection.")
        
        elif choice == 5:
            # Exit
            print("\n👋 Thank you for using Currency Converter!")
            break
        
        else:
            print("❌ Invalid option. Please try again.")

if __name__ == "__main__":
    main()
