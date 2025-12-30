def validate_symbol(symbol):
    if not symbol.isalnum():
        raise ValueError("Invalid symbol")

def validate_quantity(quantity):
    if quantity <= 0:
        raise ValueError("Quantity must be > 0")

def validate_price(price):
    if price <= 0:
        raise ValueError("Price must be > 0")
