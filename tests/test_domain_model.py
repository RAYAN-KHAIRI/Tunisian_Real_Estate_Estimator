import unittest

from domain.house import House
from domain.listing import Listing
from domain.offer import Offer
from domain.user import User


class DomainModelTests(unittest.TestCase):
    def setUp(self):
        self.seller = User(
            user_id=1,
            name="Alice",
            age=40,
            number_of_children=2,
            number_of_family_members=4,
            number_of_family_members_outside_country=1,
            profession="Engineer",
        )
        self.buyer = User(
            user_id=2,
            name="Bob",
            age=35,
            number_of_children=1,
            number_of_family_members=3,
            number_of_family_members_outside_country=0,
            profession="Teacher",
        )
        self.house = House(
            house_id=10,
            area_m2=120.5,
            rooms=4,
            region=1,
            house_type="Villa",
            standard="High",
            legal_status="non problematic",
            economic_activity=7,
            distance_to_university=3.2,
        )

    def test_house_stores_its_attributes(self):
        self.assertEqual(self.house.house_id, 10)
        self.assertEqual(self.house.area_m2, 120.5)
        self.assertEqual(self.house.rooms, 4)
        self.assertEqual(self.house.region, 1)
        self.assertEqual(self.house.house_type, "Villa")

    def test_user_can_add_house(self):
        self.seller.add_house(self.house)
        self.assertIn(self.house, self.seller.owned_houses)

    def test_user_can_create_listing_for_owned_house(self):
        self.seller.add_house(self.house)

        listing = self.seller.create_listing(
            listing_id=100,
            house=self.house,
            price=250000.0,
            title="Family villa",
            description="Close to schools",
        )

        self.assertIsInstance(listing, Listing)
        self.assertEqual(listing.creator, self.seller)
        self.assertEqual(listing.house, self.house)
        self.assertIn(listing, self.seller.created_listings)

    def test_user_cannot_create_listing_for_house_they_do_not_own(self):
        with self.assertRaises(ValueError):
            self.seller.create_listing(
                listing_id=100,
                house=self.house,
                price=250000.0,
                title="Family villa",
                description="Close to schools",
            )

    def test_buyer_can_make_offer_on_active_listing(self):
        self.seller.add_house(self.house)
        listing = self.seller.create_listing(
            listing_id=100,
            house=self.house,
            price=250000.0,
            title="Family villa",
            description="Close to schools",
        )

        offer = self.buyer.make_offer(
            offer_id=200,
            listing=listing,
            amount=240000.0,
            message="Ready to move quickly",
        )

        self.assertIsInstance(offer, Offer)
        self.assertIn(offer, listing.offers)
        self.assertEqual(offer.status, "pending")

    def test_seller_cannot_make_offer_on_own_listing(self):
        self.seller.add_house(self.house)
        listing = self.seller.create_listing(
            listing_id=100,
            house=self.house,
            price=250000.0,
            title="Family villa",
            description="Close to schools",
        )

        with self.assertRaises(ValueError):
            self.seller.make_offer(
                offer_id=200,
                listing=listing,
                amount=240000.0,
                message="My own offer",
            )

    def test_accepting_offer_marks_listing_as_sold(self):
        listing = Listing(
            listing_id=100,
            creator=self.seller,
            house=self.house,
            price=250000.0,
            title="Family villa",
            description="Close to schools",
        )
        offer = Offer(
            offer_id=200,
            buyer=self.buyer,
            listing=listing,
            amount=240000.0,
        )

        offer.accept()

        self.assertEqual(offer.status, "accepted")
        self.assertEqual(listing.status, "sold")

    def test_cannot_add_offer_to_inactive_listing(self):
        listing = Listing(
            listing_id=100,
            creator=self.seller,
            house=self.house,
            price=250000.0,
            title="Family villa",
            description="Close to schools",
            status="inactive",
        )
        offer = Offer(
            offer_id=200,
            buyer=self.buyer,
            listing=listing,
            amount=240000.0,
        )

        with self.assertRaises(ValueError):
            listing.add_offer(offer)


if __name__ == "__main__":
    unittest.main()