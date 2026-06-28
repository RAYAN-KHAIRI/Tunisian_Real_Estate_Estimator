"""
Represents a person who is interacting with the application.
a user can own houses and can create a listing. 
the attributes are based on the personal belief that they affect the real estate price. the class 
can extend to add any other attributes.
"""


class User :
     def __init__(
        self,
        user_id: int,
        name: str,
        age: int,
        number_of_children: int,
        number_of_family_members: int,
        number_of_family_members_outside_country: int,
        profession: str,
    ):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.number_of_children = number_of_children
        self.number_of_family_members = number_of_family_members
        self.number_of_family_members_outside_country = (
            number_of_family_members_outside_country
        )
        self.profession = profession

        self.owned_houses = []
        self.created_listings = []

     def add_house(self, house):
        self.owned_houses.append(house)

     def create_listing(self, listing_id: int, house, price: float, title: str, description: str):
        from .listing import Listing # avoiding circular import
        if house not in self.owned_houses:
            raise ValueError("User cannot create a listing for a house they do not own.")

        listing = Listing(
            listing_id=listing_id,
            creator=self,
            house=house,
            price=price,
            title=title,
            description=description,
        )

        self.created_listings.append(listing)
        return listing
     
     def make_offer(self, offer_id: int, listing : 'Listing', amount: float, message: str = ""):
        from .offer import Offer # avoiding circular import
        offer = Offer(
            offer_id=offer_id,
            buyer=self,
            listing=listing,
            amount=amount,
            message=message,
        )

        listing.add_offer(offer)
        return offer
