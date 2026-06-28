# domain/listing.py
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .offer import Offer 

class Listing:
    """
    A Listing is created and it contains a single house
    """
    def __init__(
        self,
        listing_id: int,
        creator,
        house,
        price: float,
        title: str,
        description: str,
        status: str = "active",
    ):
        self.listing_id = listing_id
        self.creator = creator
        self.house = house
        self.price = price
        self.title = title
        self.description = description
        self.status = status
        self.offers = []

    def add_offer(self, offer : "Offer"):
        if self.status != "active":
            raise ValueError("Cannot make an offer on an inactive or sold listing.")

        if offer.buyer == self.creator:
            raise ValueError("Seller cannot make an offer on their own listing.")

        self.offers.append(offer)

    def mark_as_sold(self):
        self.status = "sold"

    def deactivate(self):
        self.status = "inactive"