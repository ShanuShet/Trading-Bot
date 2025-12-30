import logging
from binance.enums import *
from src.validation import validate_symbol, validate_quantity, validate_price

logger = logging.getLogger(__name__)

def place_limit_order(client, symbol, side, quantity, price):
    validate_symbol(symbol)
    validate_quantity(quantity)
    validate_price(price)

    order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type=ORDER_TYPE_LIMIT,
        timeInForce=TIME_IN_FORCE_GTC,
        quantity=quantity,
        price=price
    )

    logger.info(f"Limit order placed: {order}")
    return order
