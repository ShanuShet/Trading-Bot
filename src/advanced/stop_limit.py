import logging
from binance.enums import *
from src.validation import validate_symbol, validate_quantity, validate_price

logger = logging.getLogger(__name__)

def place_stop_limit_order(client, symbol, side, quantity, stop_price, limit_price):
    validate_symbol(symbol)
    validate_quantity(quantity)
    validate_price(stop_price)
    validate_price(limit_price)

    order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type=ORDER_TYPE_STOP,
        stopPrice=stop_price,
        price=limit_price,
        quantity=quantity,
        timeInForce=TIME_IN_FORCE_GTC
    )

    logger.info(f"Stop Limit Order: {order}")
    return order
