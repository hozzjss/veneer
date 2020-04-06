from art import Art


class Listing:
    def __init__(self, art: Art, price, seller):
        self.art = art
        self.price = price
        self.seller = seller

    def __repr__(self):
        return "{art_name}, {price}.".format(
            art_name=self.art.title,
            price=self.price
        )
