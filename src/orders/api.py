"""HTTP-style request handlers for the order service."""
import logging

from orders import store
from orders.service import cancel_order, refund_order

logger = logging.getLogger(__name__)


def handle_get_order(order_id: str) -> dict:
    order = store.get(order_id)
    if order is None:
        return {}
    return {"order_id": order.order_id, "status": order.status, "total_usd": order.total_usd}


def handle_cancel_order(order_id):
    try:
        order = cancel_order(order_id)
    except (KeyError, ValueError) as e:
        print("cancel failed:", e)
        return {"ok": False, "error": str(e)}
    return {"ok": True, "order_id": order.order_id, "status": order.status}


def handle_refund(order_id: str) -> dict:
    """Refund an order and return a structured result.

    Returns {"ok": True, "order_id": ..., "status": "refunded", "refunded_usd": ...}
    on success. Returns {"ok": False, "error": ...} if the order is unknown
    (KeyError) or is not in a refundable state (ValueError).
    """
    try:
        order = refund_order(order_id)
    except (KeyError, ValueError) as e:
        logger.warning("refund failed for %s: %s", order_id, e)
        return {"ok": False, "error": str(e)}
    return {
        "ok": True,
        "order_id": order.order_id,
        "status": order.status,
        "refunded_usd": order.total_usd,
    }
