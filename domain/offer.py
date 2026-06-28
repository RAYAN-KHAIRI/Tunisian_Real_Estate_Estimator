# domain/offer.py
from typing import TYPE_CHECKING
if TYPE_CHECKING :
    from .listing import Listing
    from .user import User
    
class Offer:
    """
    Represents a buyer's offer on a listing.
    """

    def __init__(
        self,
        offer_id: int,
        buyer,
        listing,
        amount: float,
        message: str = "",
        status: str = "pending",
    ):
        self.offer_id = offer_id
        self.buyer = buyer
        self.listing = listing
        self.amount = amount
        self.message = message
        self.status = status

    def accept(self):
        self.status = "accepted"
        self.listing.mark_as_sold()

    def reject(self):
        self.status = "rejected"