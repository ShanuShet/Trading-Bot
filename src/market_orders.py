import logging
from binance.enums import *
from src.validation import validate_symbol, validate_quantity

logger = logging.getLogger(__name__)

def place_market_order(client, symbol, side, quantity):
    validate_symbol(symbol)
    validate_quantity(quantity)

    order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type=ORDER_TYPE_MARKET,
        quantity=quantity
    )

    logger.info(f"Market order: {order}")
    return order
