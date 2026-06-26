class House:
    """
    Represents a house in our real estate Market. The features
    are brain stormed by Rayan Khairi's expertise in the tunisian
    Market. 
    the region Attribute is an int ranging from 1 to 24 with each
    number representing a tunisian state. 
    house_type is in {"Villa" , "Duplex", "Appartement"}. This may
    be very relevant for the tunisian costumer because of many
    social factors.
    standard is in {"low", "moderate", "High", "luxurious"}
    legal_status is in {"Problematic", "non problematic"} which
    comes also from tunisian context.
    economic_activity in {1,10}
    Other features shall be added Later on.
    """
    def __init__(
        self,
        house_id: int,
        area_m2: float,
        rooms: int,
        region: int,
        house_type: str,
        standard: str,
        legal_status: str,
        economic_activity: int,
        distance_to_university: float,
        asking_price: float,
    ):
        self.house_id = house_id
        self.area_m2 = area_m2
        self.rooms = rooms
        self.region = region
        self.house_type = house_type
        self.standard = standard
        self.legal_status = legal_status
        self.economic_activity = economic_activity
        self.distance_to_university = distance_to_university
        self.asking_price = asking_price

